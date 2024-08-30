import tkinter as tk
from tkinter import messagebox
from pytubefix import YouTube
from pytubefix.cli import on_progress
import sys
import io

# Set default encoding for the environment
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# Path where videos will be saved
SAVE_PATH = r"C:\Users\test\OneDrive\Documents\PYTHON"  # Update as needed

def download_video():
    url = entry.get().strip()  # Get and clean the URL input
    if not url:
        messagebox.showerror("Input Error", "Please enter a YouTube URL.")
        return
    
    print(f"Processing URL: '{url}'")  # Print the URL for debugging
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"Video title: {yt.title}")  # Print the video title for debugging
        
        # Get the video with the highest resolution
        ys = yt.streams.get_highest_resolution()
        print(f"Downloading stream with resolution: {ys.resolution}")  # Debug resolution
        
        # Download the video
        ys.download(output_path=SAVE_PATH)
        status_label.config(text="Video downloaded successfully!")
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        status_label.config(text=f"Download Failed: {str(e)}")
        messagebox.showerror("Download Error", f"Download Failed: {str(e)}")
        print(f"Error: {str(e)}")  # Print error for debugging

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create a canvas
canvas = tk.Canvas(root, width=400, height=300, relief='raised')
canvas.pack()

# Create and place the title label
title_label = tk.Label(root, text='YouTube Video Downloader', font=('Helvetica', 14))
canvas.create_window(200, 25, window=title_label)

# Create and place the URL entry label
url_label = tk.Label(root, text='Enter Video URL:', font=('Helvetica', 10))
canvas.create_window(200, 100, window=url_label)

# Create and place the URL entry field
entry = tk.Entry(root, width=50)
canvas.create_window(200, 140, window=entry)

# Create and place the download button
download_button = tk.Button(root, text='Download', command=download_video, bg='brown', fg='white', font=('Helvetica', 10, 'bold'))
canvas.create_window(200, 180, window=download_button)

# Create and place the status label
status_label = tk.Label(root, text='', font=('Helvetica', 10))
canvas.create_window(200, 220, window=status_label)

# Run the main event loop
root.mainloop()
