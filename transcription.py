import json
from youtube_transcript_api import YouTubeTranscriptApi

# Function to get transcript and save it to a JSON file
def save_transcript_to_json(video_id, filename):
    try:
        # Step 2: Retrieve the transcription
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Step 3: Save the transcription to a JSON file
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(transcript, f, ensure_ascii=False, indent=4)
        
        print(f"Transcript saved to {filename}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
video_id = "videoid"  # Replace with your video ID
filename = "filename"
save_transcript_to_json(video_id, filename)
