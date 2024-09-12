import os
import pygame
import tkinter as tk
from tkinter import filedialog

# Initialize pygame mixer
pygame.mixer.init()

# Function to load and play the selected song
def play_song():
    song = filedialog.askopenfilename(initialdir="C:/", title="Select a Song", filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
    if song:
        song_label.config(text=os.path.basename(song))  # Update the label to show the song name
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)  # Play the selected song

# Function to pause the current song
def pause_song():
    pygame.mixer.music.pause()

# Function to resume the paused song
def resume_song():
    pygame.mixer.music.unpause()

# Function to stop the music
def stop_song():
    pygame.mixer.music.stop()

# Create the main window
root = tk.Tk()
root.title("Simple Music Player")

# Create GUI elements
song_label = tk.Label(root, text="No Song Playing", font=("Arial", 14))
song_label.pack(pady=10)

play_button = tk.Button(root, text="Play Song", command=play_song, width=10, font=("Arial", 14))
play_button.pack(pady=10)

pause_button = tk.Button(root, text="Pause", command=pause_song, width=10, font=("Arial", 14))
pause_button.pack(pady=10)

resume_button = tk.Button(root, text="Resume", command=resume_song, width=10, font=("Arial", 14))
resume_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=stop_song, width=10, font=("Arial", 14))
stop_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
