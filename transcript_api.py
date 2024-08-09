from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable


class YouTubeTranscriptModule:
    def __init__(self):
        self.formatter = TextFormatter()

    def fetch_transcript(self, video_id):
        """
        Fetches the transcript of a given video.

        :param video_id: The YouTube video ID.
        :return: The transcript as a string.
        """
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
            return self.formatter.format_transcript(transcript_list)
        except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable) as e:
            return f"Transcript not available: {str(e)}"

    def fetch_transcript_in_language(self, video_id, language_code='en'):
        """
        Fetches the transcript in a specific language. If not available, attempts to translate.

        :param video_id: The YouTube video ID.
        :param language_code: The preferred language code (e.g., 'en' for English).
        :return: The transcript in the specified language, or translated if not available.
        """
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language_code])
            return self.formatter.format_transcript(transcript)
        except NoTranscriptFound:
            try:
                transcript = YouTubeTranscriptApi.get_transcript(video_id)
                return self.formatter.format_transcript(transcript)
            except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable) as e:
                return f"Transcript not available: {str(e)}"

    def fetch_transcript_with_fallback(self, video_id, preferred_language_code='en'):
        """
        Manages cases where transcripts are not available in the preferred language.

        :param video_id: The YouTube video ID.
        :param preferred_language_code: The preferred language code (e.g., 'en' for English).
        :return: The transcript in the preferred language, or falls back to another language if needed.
        """
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[preferred_language_code])
            return self.formatter.format_transcript(transcript)
        except NoTranscriptFound:
            try:
                transcript = YouTubeTranscriptApi.list_transcripts(video_id)
                available_languages = transcript.get_languages()

                for lang in available_languages:
                    try:
                        transcript = transcript.find_transcript([lang['language_code']])
                        return self.formatter.format_transcript(transcript.fetch())
                    except NoTranscriptFound:
                        continue

                return "No transcripts available in any language."
            except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable) as e:
                return f"Transcript not available: {str(e)}"
yt_transcript = YouTubeTranscriptModule()

# Fetch a transcript in any available language
#print(yt_transcript.fetch_transcript('6i3EGqOBRiU'))

# Fetch a transcript in English
#print(yt_transcript.fetch_transcript_in_language('6i3EGqOBRiU', 'en'))

# Fetch a transcript with fallback to any available language
print(yt_transcript.fetch_transcript_with_fallback('6i3EGqOBRi', 'en'))
