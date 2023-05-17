import pytube
import os
import tkinter as tk
from tkinter import filedialog

def download_video():
    url = entry_url.get()
    output_path = entry_output.get()

    if not os.path.exists(output_path):
        status_text.set("Invalid output directory path.")
        return

    try:
        video = pytube.YouTube(url)

        stream = video.streams.get_highest_resolution()

        video_title = video.title

        status_text.set(f"Downloading video: {video_title}")

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

window = tk.Tk()
window.title("YouTube Downloader(IT SCHOOL PROJECT)")
window.configure(bg="white")

label_url = tk.Label(window, text="YouTube Video URL:", bg="white", fg="red")
label_url.pack()

url_frame = tk.Frame(window, bg="white")
url_frame.pack()

entry_url = tk.Entry(url_frame, width=50)
entry_url.pack(side=tk.LEFT)

paste_button = tk.Button(url_frame, text="Paste", command=paste_url, bg="red", fg="white")
paste_button.pack(side=tk.LEFT)

label_output = tk.Label(window, text="Where do you want to save it:", bg="white", fg="red")
label_output.pack()
entry_output = tk.Entry(window, width=50)
entry_output.pack()
button_browse = tk.Button(window, text="Browse", command=select_output_directory, bg="red", fg="white")
button_browse.pack()

button_download = tk.Button(window, text="Get it!!", command=download_video, bg="red", fg="white")
button_download.pack()

status_text = tk.StringVar()
status_label = tk.Label(window, textvariable=status_text, bg="white", fg="red")
status_label.pack()

window.mainloop()
