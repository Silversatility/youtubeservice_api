import os 

from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from googleapiclient.discovery import build

from .serializers import VideoSerializer

YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")


class VideoListAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = "video_list.html"

    def get(self, request):
        q = request.query_params.get("query", "")
        youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
        search_request = youtube.search().list(
            part="snippet",
            type="video",
            maxResults=2,
            q=q,
        )
        search_response = search_request.execute()

        video_ids = [item["id"]["videoId"] for item in search_response["items"]]
        video_request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=",".join(video_ids),
        )
        video_response = video_request.execute()

        videos = []
        for item in video_response["items"]:
            video_data = {
                "title": item["snippet"]["title"],
                "description": item["snippet"]["description"],
                "video_id": item["id"],
                "thumbnail_url": item["snippet"]["thumbnails"]["high"]["url"],
                "views_count": item["statistics"]["viewCount"],
                "author_name": item["snippet"]["channelTitle"],
            }
            videos.append(video_data)

        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            context = {"videos": videos}
            return JsonResponse(context)

        serializer = VideoSerializer(videos, many=True)
        context = {"videos": serializer.data}
        return Response(context)
