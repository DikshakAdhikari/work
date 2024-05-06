import requests
from transcript import deepGram_api_call, AUDIO_URL

transcriptt= deepGram_api_call(audio_url=AUDIO_URL)
# print(transcriptt.json())

import requests

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/Ki0d7PgIFmOFh5dsrj4L"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": "0f228ef5c798c019a23ca4b8715e9982"
}

data = {
  "text": "Born and raised in the charming south, I can add a touch of sweet southern hospitality to your audiobooks and podcasts",
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
  }
}

response = requests.post(url, json=data, headers=headers)
with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)
