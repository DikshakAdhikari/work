from pytube import YouTube 

def extractAudio(url, location):
    try:
        yt= YouTube(url)
        audio_stream= yt.streams.filter(only_audio= True).first()
        audio_stream.download(location)
        print("Audio extraction completed successfully")

    except Exception as e:
        
        print("Error: ", e)

if __name__ == "__main__":
    url= "https://www.youtube.com/watch?v=iiaH2q-RlDs"
    location= "./sound"

    extractAudio(url, location)