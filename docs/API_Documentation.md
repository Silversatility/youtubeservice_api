# API Documentation for YouTube Service API

## Overview

The YouTube Service API allows easy access to YouTube video data, providing tools for searching videos, fetching detailed information about specific videos, and generating suggestions based on user queries.

## Endpoints

### Search Videos

- **Endpoint:** `/api/videos/`
- **Method:** `GET`
- **Description:** Returns a list of videos based on the search query.
- **Query Parameters:**
  - `query` (string): The search keyword or phrase.
  - `max_results` (optional, int): Maximum number of results to return.
- **Success Response:**
  - **Code:** 200 OK
  - **Content Example:**
    ```json
    [
      {
        "title": "Django Tutorial",
        "description": "Learn Django web framework.",
        "video_id": "dQw4w9WgXcQ",
        "thumbnail_url": "http://example.com/thumbnail.jpg",
        "views_count": "4083967",
        "author_name": "freeCodeCamp.org"
      }
    ]
    ```

## Error Handling

- **Code:** 400 Bad Request
- **Content:** `{ "error": "Missing or invalid parameters" }`

- **Code:** 404 Not Found
- **Content:** `{ "error": "Resource not found" }`

- **Code:** 500 Internal Server Error
- **Content:** `{ "error": "Internal server error" }`
