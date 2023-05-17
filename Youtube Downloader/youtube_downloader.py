import pytube
import os
import tkinter as tk
from tkinter import filedialog

def download_video():
    url = entry_url.get()
    output_path = entry_output.get()

    # Validate the output path
    if not os.path.exists(output_path):
        status_text.set("Invalid output directory path.")
        return

    try:
        # Create a YouTube object with the video URL
        video = pytube.YouTube(url)

        # Choose the highest resolution available
        stream = video.streams.get_highest_resolution()

        # Get the video title for display purposes
        video_title = video.title

        # Provide feedback to the user
        status_text.set(f"Downloading video: {video_title}")

        # Download the video to the specified output path
        stream.download(output_path)

        status_text.set("Download complete!")

    except pytube.exceptions.PytubeError as e:
        status_text.set("An error occurred while downloading the video:\n" + str(e))

def select_output_directory():
    output_path = filedialog.askdirectory()
    entry_output.delete(0, tk.END)
    entry_output.insert(tk.END, output_path)

def paste_url():
    url = window.clipboard_get()
    entry_url.delete(0, tk.END)
    entry_url.insert(tk.END, url)

# Create the main application window
window = tk.Tk()
window.title("YouTube Downloader")
window.configure(bg="white")

# Create URL input label and entry field
label_url = tk.Label(window, text="YouTube Video URL:", bg="white", fg="red")
label_url.pack()

url_frame = tk.Frame(window, bg="white")
url_frame.pack()

entry_url = tk.Entry(url_frame, width=50)
entry_url.pack(side=tk.LEFT)

paste_button = tk.Button(url_frame, text="Paste", command=paste_url, bg="red", fg="white")
paste_button.pack(side=tk.LEFT)

# Create output directory input label, entry field, and browse button
label_output = tk.Label(window, text="Output Directory:", bg="white", fg="red")
label_output.pack()
entry_output = tk.Entry(window, width=50)
entry_output.pack()
button_browse = tk.Button(window, text="Browse", command=select_output_directory, bg="red", fg="white")
button_browse.pack()

# Create download button
button_download = tk.Button(window, text="Download", command=download_video, bg="red", fg="white")
button_download.pack()

# Create status label for feedback
status_text = tk.StringVar()
status_label = tk.Label(window, textvariable=status_text, bg="white", fg="red")
status_label.pack()

# Start the GUI event loop
window.mainloop()
