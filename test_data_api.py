from youtube_wrapper import YouTubeDataAPI

# Initialize with your YouTube Data API key
api_key = 'AIzaSyAmCqi3FtXYJ-9HYCrNJertqCFxofhuzUc'
youtube_api = YouTubeDataAPI(api_key)

# Get details of a specific video
#video_id = '6i3EGqOBRiU'  # Example video ID
#video_details = youtube_api.get_video_details(video_id)
#print("Video Details:", video_details)

# Search for videos based on a keyword
#search_results = youtube_api.search_videos('Introduction to Python Course|Python for beginners', max_results=3)
#print("Search Results:", search_results)
#print(len(search_results))

# List videos in a specific YouTube channel
channel_id = 'UCM-yUTYGmrNvKOCcAl21g3w'  # Example channel ID (freeCodeCamp.org)
channel_videos = youtube_api.list_channel_videos(channel_id, max_results=3)
print("Channel Videos:", channel_videos)

