# Youtube Search

The name of the project is Youtube Search


## Description

The project is used to showcase the use of youtube api. To search for videos in youtube, get results of you search and embed them in a django project.   


## Technologies Used

- Django
- Python3
- Youtube Api


## Installation

- First go to Google Developers page login and create a new project.
    [Google developer](https://console.developers.google.com/)

- Then go to Enable Api and Services and find YouTube Data API-v3, enable it, then create credentials then you will get the youtube api key.
- Git clone the project in you repository
    ```
    git clone https://github.com/Silversatility/youtubeservice_api.git
    ```
- Create an .env file in the root of the project 
    ```
    YOUTUBE_API_KEY='<your-youtube-api-key>'
    ```
- Create a virtual environment and run it
    ```
    virtualenv virtual
    
    source virtual/bin/activate
    ```
- Install dependencies in the requirements.txt file
    ```
    pip install -r requirements.txt
    ```
- Run the application
    ```
    python3 manage.py runserver
    ```