import pygame
import time

CLEAR = "\033[2j"
CLEAR_AND_RETURN = "\033[H"

def initialize_sound():
    try:
        pygame.mixer.init()
        print("Library initialized successfully.")
    except pygame.error:
        print("Error initializing the library.")

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minute_left = time_left // 60
        second_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minute_left:02d}:{second_left:02d}")
    
    try:
        pygame.mixer.music.load("Alarm.mp3")
        print("Audio file loaded successfully.")
    except pygame.error:
        print("Error loading the audio file.")

    try:
        pygame.mixer.music.play()
        print("Audio file played successfully.")
    except pygame.error:
        print("Error playing the audio file.")

    # Delay for 5 seconds to let the alarm play
    time.sleep(5)

def main():
    minutes = int(input("How many minutes to wait: "))
    seconds = int(input("How many seconds to wait: "))
    total_seconds = minutes * 60 + seconds

    initialize_sound()
    alarm(total_seconds)

if __name__ == "__main__":
    main()
