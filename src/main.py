import os
import threading
import tkinter
import time

from PIL import Image, ImageTk
from tkinter import ttk


PADDING = 20  # Top-right padding
GIF_SIZE = 1  # Size multiplier
GIF_SPEED = 1

# Dont change
SIZE_WIDTH = int(220 * GIF_SIZE)
SIZE_HEIGHT = int(391 * GIF_SIZE)


class App(tkinter.Tk): 
    def __init__(self):
        super().__init__()
        
        self.geometry(f"{SIZE_WIDTH}x{SIZE_HEIGHT}+{self.winfo_screenwidth()-(SIZE_WIDTH+PADDING)}+{PADDING}")
        self.attributes("-topmost", True)
        self.overrideredirect(True)

        self._gif_frames = []

        self._video_label = ttk.Label(self)
        self._video_label.pack()

        self._read_gif_frames()

        thread = threading.Thread(target=self._stream_video, daemon=True)
        thread.start()
    
    def _stream_video(self):
        while True:
            for frame in self._gif_frames:
                self._video_label.config(image=frame),
                self._video_label.image = frame
                time.sleep(.1 / GIF_SPEED)

    def _read_gif_frames(self):
        gif = Image.open(os.path.join(os.path.dirname(__file__), "subway_surfers.gif"))
        for i in range(gif.n_frames):
            gif.seek(i)
            frame = gif.copy()
            frame = frame.resize((SIZE_WIDTH, SIZE_HEIGHT))
            self._gif_frames.append(ImageTk.PhotoImage(frame))


if __name__ == '__main__':
    App().mainloop()
