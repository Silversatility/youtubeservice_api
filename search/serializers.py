# serializers.py in your Django app

from rest_framework import serializers


class VideoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=None)
    description = serializers.CharField(max_length=None)
    video_id = serializers.CharField(max_length=None)
    thumbnail_url = serializers.SerializerMethodField()
    video_url = serializers.SerializerMethodField()
    views_count = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()

    def get_thumbnail_url(self, obj):
        return "URL to the thumbnail based on the video_id"

    def get_video_url(self, obj):
        return f"https://www.youtube.com/watch?v={obj['video_id']}"

    def get_views_count(self, obj):
        return "Number of views for the video"

    def get_author_name(self, obj):
        return "Author's name of the video"
