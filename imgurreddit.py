import praw
from imgurpython import ImgurClient
from google.cloud import texttospeech

def imgur():
    client_id = "client_id"
    client_secret = "client_secret"

    client = ImgurClient(client_id,client_secret)

    response = client.upload_from_path("video.avi")
    print(response["link"])
    return response["link"]

def reddit(link,caption):
    reddit = praw.Reddit(client_id="client_id",
                         client_secret="secret",
                         user_agent="For posting recorded videos of a chair falling apart to a custom subreddit.",
                         username="username",
                         password="password")

    subreddit = reddit.subreddit("owiehack")
    subreddit.submit(title=caption,url=str(link[:-1]))

def tts(caption):
    #code from gcp example for tts
    

    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=caption)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open("speak.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "speak.mp3"')
