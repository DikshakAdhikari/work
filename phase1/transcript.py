from deepgram import DeepgramClient, PrerecordedOptions
from getAudio import extractAudio
from dotenv import load_dotenv
import os
import requests

load_dotenv()

extractAudio(url="https://www.youtube.com/watch?v=iiaH2q-RlDs", location="./subtitles")

AUDIO_URL = 'https://static.deepgram.com/examples/Bueller-Life-moves-pretty-fast.wav'
DEEPGRAM_API_KEY = os.getenv("API_KEY")


def deepGram_api_call(audio_url):
    url = "https://api.deepgram.com/v1/listen"
    headers = {
    "Authorization": "Token "+ DEEPGRAM_API_KEY,
    "content-type": "application/json"
    }
    data = {
    "url": audio_url,
    "smart_format": True,
    "model": "nova-2",
    "language": "en-GB"
    }

    response = requests.post(url, headers=headers, json=data)
    return response


def main():
    
    transcripted_result= deepGram_api_call(audio_url= AUDIO_URL)
    print(transcripted_result.json())

   
if __name__ == '__main__':
    main()