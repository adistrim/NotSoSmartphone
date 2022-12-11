import pygame
import os
from tkinter import *


def play_music():
    class MusicPlayer:
        def __init__(self, esp):
            pygame.init()
            pygame.mixer.init()
            self.root = esp
            self.root.geometry("395x220")
            self.root.title("Music Player")
            self.status = StringVar()
            self.track = StringVar()
            self.status.set("-Stopped")
            controls = LabelFrame(self.root, font=("Calibre", 15, "bold"), bg="white", fg="black", bd=10)
            controls.place(x=0, y=0, width=150, height=220)
            Button(controls, text="PLAY", command=self.start_playing, width=7, height=1, font=("Calibre", 16, "bold"),
                   fg="white").grid(row=0, column=0, padx=10, pady=5)
            Button(controls, text="PAUSE", command=self.pause, width=7, height=1, font=("Calibre", 16, "bold"),
                   fg="white").grid(row=1, column=0, padx=10, pady=5)
            Button(controls, text="RESUME", command=self.resume, width=7, height=1, font=("Calibre", 16, "bold"),
                   fg="white").grid(row=2, column=0, padx=10, pady=5)
            Button(controls, text="STOP", command=self.stop_playing, width=7, height=1, font=("Calibre", 16, "bold"),
                   fg="white").grid(row=3, column=0, padx=10, pady=5)
            Button(controls, text="EXIT", command=self.quit_program, width=5, height=1, font=("Calibre", 16, "bold"),
                   fg="red").grid(row=4, column=0, padx=10, pady=5)
            songs_frame = LabelFrame(self.root, text="Playlist", font=("Calibre", 15, "bold"), bg="white", fg="black",
                                     bd=10)
            songs_frame.place(x=145, y=0, width=250, height=220)
            self.playlist = Listbox(songs_frame, selectbackground="blue", selectmode=SINGLE,
                                    font=("Calibre", 12, "bold"), bg="white", fg="blue")
            self.playlist.pack(fill=BOTH)
            os.chdir("songs")
            song_tracks = os.listdir()
            for track in song_tracks:
                self.playlist.insert(END, track)
                continue

        @staticmethod
        def quit_program():
            root.destroy()

        def start_playing(self):
            if self.status.get() == "-Stopped":
                self.track.set(self.playlist.get(ACTIVE))
                self.status.set("-Playing")
                pygame.mixer.music.load(self.playlist.get(ACTIVE))
                pygame.mixer.music.play()

        def pause(self):
            if self.status.get() == "-Playing":
                self.status.set("-Paused")
                pygame.mixer.music.pause()

        def resume(self):
            if self.status.get() == "-Paused":
                self.status.set("-Playing")
                pygame.mixer.music.unpause()

        def stop_playing(self):
            if self.status.get() == "-Playing":
                self.status.set("-Stopped")
                pygame.mixer.music.stop()

    root = Tk()
    MusicPlayer(root)
    root.mainloop()
    pygame.quit()
