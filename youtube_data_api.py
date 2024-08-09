from googleapiclient.discovery import build

class YouTubeDataAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def get_video_details(self, video_id):
        """
        Retrieve details for a specific video.
        
        :param video_id: The ID of the video to retrieve details for.
        :return: A dictionary with video details (title, description, view count, like count).
        """
        request = self.youtube.videos().list(
            part='snippet,statistics',
            id=video_id
        )
        response = request.execute()
        if response['items']:
            item = response['items'][0]
            video_details = {
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'view_count': item['statistics'].get('viewCount', 'N/A'),
                'like_count': item['statistics'].get('likeCount', 'N/A'),
                'dislike_count': item['statistics'].get('dislikeCount', 'N/A'),
                'comment_count': item['statistics'].get('commentCount', 'N/A')
            }
            return video_details
        return None

    def search_videos(self, query, max_results=5):
        """
        Search for videos on YouTube based on a keyword.
        
        :param query: The search query string.
        :param max_results: The maximum number of results to return.
        :return: A list of video details (title, video ID).
        """
        request = self.youtube.search().list(
            part='snippet',
            q=query,
            type='video',
            maxResults=max_results
        )
        response = request.execute()
        search_results = []
        for item in response['items']:
            video_data = {
                'video_id': item['id']['videoId'],
                'title': item['snippet']['title'],
                'description': item['snippet']['description']
            }
            search_results.append(video_data)
        return search_results

    def list_channel_videos(self, channel_id, max_results=5):
        """
        List the videos in a specific YouTube channel.
        
        :param channel_id: The ID of the YouTube channel.
        :param max_results: The maximum number of videos to return.
        :return: A list of video details (title, video ID).
        """
        request = self.youtube.search().list(
            part='snippet',
            channelId=channel_id,
            maxResults=max_results,
            order='date'
        )
        response = request.execute()
        video_list = []
        for item in response['items']:
            video_data = {
                'video_id': item['id']['videoId'],
                'title': item['snippet']['title'],
                'description': item['snippet']['description']
            }
            video_list.append(video_data)
        return video_list
