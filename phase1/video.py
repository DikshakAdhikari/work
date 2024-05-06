from pytube import YouTube 

def download_video(url, save_path):
    try:
      
        yt = YouTube(url)
        
        stream = yt.streams.get_highest_resolution()
     
        stream.download(output_path=save_path)
        
        print("Download completed successfully!")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=iiaH2q-RlDs"  
    save_location = "./downloads" 
    
    download_video(video_url, save_location)
