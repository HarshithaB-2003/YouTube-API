from youtube_transcript_api_wrapper.transcript_api import YouTubeTranscriptModule
yt_transcript = YouTubeTranscriptModule()

# Fetch a transcript in any available language
print(yt_transcript.fetch_transcript('VIDEO_ID'))

# Fetch a transcript in English
print(yt_transcript.fetch_transcript_in_language('VIDEO_ID', 'en'))

# Fetch a transcript with fallback to any available language
print(yt_transcript.fetch_transcript_with_fallback('VIDEO_ID', 'en'))
