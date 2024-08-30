from pytube import YouTube

url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # Replace with your test URL

try:
    obj = YouTube(url)
    print("Video title:", obj.title)
except Exception as e:
    print(f"Error: {str(e)}")
