import time
import datetime
import pygame

def set_alarm(alarm_time):

    print(f"Alarm set for {alarm_time}")
    print()

    sound_file = "03. Hope Is the Thing With Feathers.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {current_time}")

        if current_time == alarm_time:
            print("\n" + "-" * 45)
            print("WAKE UP! Alarm time reached.")
            print("Playing alarm sound...")
            print("-" * 45 + "\n")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play(loops= -1)
            while is_running:
                stop = input()
                if stop.lower() == 'q':
                    pygame.mixer.music.stop()
                    print("\nAlarm stopped.")
                    break

            is_running = False

        time.sleep(1)

if __name__ == '__main__':
    print("=" * 45)
    print("            SIMPLE ALARM CLOCK")
    print("=" * 45)
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)