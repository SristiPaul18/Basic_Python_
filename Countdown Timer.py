import time

print("=" * 40)
print("            COUNTDOWN TIMER            ")
print("=" * 40)

my_time = int(input("Enter the time in seconds: "))
print("-" * 40)
print("Timer Started...\n")

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int( x / 60) % 60
    hours = int( x / 3600 )
    print(f"Time Remaining:  {hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("\n" + "=" * 40)
print("               TIME IS UP!!             ")
print("=" * 40)
