import praw
from imgurpython import ImgurClient
from google.cloud import texttospeech

def imgur():
    client_id = "9c5e85230d3df52"
    client_secret = "3d722b8f08385aef8ebb92c284457325ecb15347"

    client = ImgurClient(client_id,client_secret)

    response = client.upload_from_path("video.avi")
    print(response["link"])
    return response["link"]

def reddit(link,caption):
    reddit = praw.Reddit(client_id="DHIiBuNzG_WkAQ",
                         client_secret="og2LS94QeZ45FBweeuE_RHVa1eg",
                         user_agent="For posting recorded videos of a chair falling apart to a custom subreddit.",
                         username="owiehack",
                         password="drewee602")

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
