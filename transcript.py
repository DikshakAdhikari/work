from deepgram import DeepgramClient, PrerecordedOptions
from getAudio import extractAudio
from dotenv import load_dotenv
import os

load_dotenv()

extractAudio(url="https://www.youtube.com/watch?v=iiaH2q-RlDs", location="./subtitles")


DEEPGRAM_API_KEY = os.getenv("API_KEY")
print(DEEPGRAM_API_KEY)


AUDIO_URL = {
  'url': 'https://static.deepgram.com/examples/Bueller-Life-moves-pretty-fast.wav'
}

def main():
    deepgram = DeepgramClient(DEEPGRAM_API_KEY)

    options = PrerecordedOptions(
        smart_format=True, model="nova-2", language="en-GB"
    )

    print('Requesting transcript...')
    print('Your file may take up to a couple minutes to process.')
    print('While you wait, did you know that Deepgram accepts over 40 audio file formats? Even MP4s.')
    print('To learn more about customizing your transcripts check out developers.deepgram.com')

    response = deepgram.listen.prerecorded.v('1').transcribe_url(AUDIO_URL, options)
    print(response.to_json(indent=4))

if __name__ == '__main__':
    main()