import random

words = (
    "apple", "banana", "grapes", "orange", "peach", "doctor", "teacher", "engineer", "lawyer", "singer",
    "tiger", "elephant", "giraffe", "monkey", "rabbit", "computer", "keyboard", "monitor", "laptop", "mouse",
    "desert", "island", "mountain", "village", "forest", "puzzle", "pirate", "rocket", "dragon", "camera",
    "airplane", "bicycle", "universe", "sunshine", "moonlight", "rainbow", "waterfall", "volcano", "glacier", "canyon",
    "ocean", "river", "lake", "beach", "desert", "jungle", "savanna", "forest", "meadow", "hill",
    "valley", "mountain", "plateau", "cave", "canyon", "cliff", "waterfall", "island", "peninsula", "reef",
    "coral", "seashell", "starfish", "octopus", "whale", "dolphin", "shark", "seal", "turtle", "jellyfish",
    "crab", "lobster", "squid", "starfish", "seahorse", "algae", "plankton", "kelp", "seabed", "tidal",
    "tsunami", "hurricane", "earthquake", "volcano", "tornado", "flood", "drought", "landslide", "avalanche",
    "wildfire", "blizzard", "thunderstorm", "hailstorm", "cyclone", "typhoon", "monsoon", "rain", "snow", "sleet", "fog",
    "mist", "dew", "humidity", "temperature", "barometer", "thermometer", "anemometer", "rain gauge", "weather",
    "climate", "forecast", "meteorology", "atmosphere", "troposphere", "stratosphere", "mesosphere", "thermosphere",
    "exosphere", "ozone", "greenhouse", "carbon", "oxygen", "nitrogen", "helium", "hydrogen", "argon", "neon", "krypton",
    "xenon", "radon", "plasma", "ionosphere", "aurora", "northern lights", "sun", "moon", "planet", "star",
    "galaxy", "universe", "nebula", "asteroid", "comet", "meteor", "black hole", "supernova", "quasar", "pulsar",
    "constellation", "zodiac", "eclipse", "solstice", "equinox", "telescope", "observatory", "astronomy",
    "astrophysics", "cosmology", "space", "NASA", "astronaut", "spaceship", "satellite", "rocket", "launch", "mission", "orbit", "gravity",
    "weight", "mass", "force", "acceleration", "velocity", "speed", "distance", "time", "energy", "power",
    "work", "machine", "simple machine", "lever", "pulley", "inclined plane", "wheel and axle", "screw", "wedge", "mechanics",
    "thermodynamics", "kinetics", "dynamics", "statics", "fluid dynamics", "hydraulics", "pneumatics", "electricity",
    "magnetism", "electromagnetism", "circuit", "voltage", "current", "resistance", "power", "energy", "battery", "capacitor", "inductor", "transistor",
    "diode", "LED", "solar cell", "generator", "alternator", "transformer", "conductor", "insulator", "semiconductor",
    "superconductor", "electronic", "digital", "analog", "signal", "wave", "frequency", "amplitude", "phase", "interference", "resonance",
    "radio", "television", "telephone", "internet", "computer", "laptop", "tablet", "smartphone", "smartwatch",
    "wearable", "device", "gadget", "technology", "innovation", "invention", "discovery", "research", "development", "engineering",
    "science", "mathematics", "physics", "chemistry", "biology", "geology", "astronomy", "psychology", "sociology", "anthropology",
    "economics", "political science", "history", "geography", "philosophy", "literature", "art", "music", "theater", "dance", "film",
    "photography", "sculpture", "architecture", "design", "fashion", "craft", "painting", "drawing", "printmaking",
    "calligraphy", "ceramics", "pottery", "textiles", "jewelry", "metalwork", "woodworking", "glassblowing", "mosaic", "collage",
    "installation", "performance art", "conceptual art", "abstract art", "realism", "impressionism", "expressionism", "surrealism",
    "cubism", "pop art", "minimalism", "art deco", "art nouveau", "renaissance", "baroque", "rococo", "gothic", "romanesque", "neoclassical", "modernism",
    "postmodernism", "contemporary art", "museum", "gallery", "exhibition", "curator", "collection", "artist", "sculptor", "painter", "photographer",
    "designer", "architect", "engineer", "scientist", "researcher", "teacher", "student", "professor", "doctor", "nurse",
    "therapist", "psychologist", "social worker", "lawyer", "judge", "politician", "activist", "entrepreneur", "businessperson",
    "manager", "employee", "worker", "laborer", "farmer", "fisherman", "hunter", "chef", "waiter", "bartender", "driver", "pilot", "mechanic",
    "electrician", "plumber", "carpenter", "builder", "architect", "designer", "artist", "musician", "actor", "dancer",
    "writer", "journalist", "editor", "publisher", "librarian", "researcher", "scientist", "engineer", "technician",
    "analyst", "consultant", "advisor", "counselor", "coach", "trainer", "mentor", "tutor", "instructor", "professor", "teacher",
    "student", "learner", "pupil", "scholar", "graduate", "undergraduate")

hangman_art = {
    0: ("     ", "      ", "      "),
    1: ("   o  ", "      ", "      "),
    2: ("   o  ", "   |  ", "      "),
    3: ("   o  ", "  /|  ", "      "),
    4: ("   o  ", "  /|\\ ", "      "),
    5: ("   o  ", "  /|\\ ", "  /   "),
    6: ("   o  ", "  /|\\ ", "  / \\ ")
}

def display_man(wrong_guesses):
    print("\n   HANGMAN")
    print("  ---------")
    for line in hangman_art[wrong_guesses]:
        print(" |" + line)
    print(" |")
    print("_|_______")

def display_hint(hint):
    print("\nWord: " + " ".join(hint))

def display_answer(answer):
    print("\nThe correct word was: " + " ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    print("=" * 45)
    print("           WELCOME TO HANGMAN GAME")
    print("     Guess the word before it’s too late!")
    print("=" * 45)

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters))}")
        print("-" * 45)

        guess = input("Enter a Letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses = wrong_guesses + 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("\nCongratulations! You guessed the word!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("\nGame Over! Better luck next time.")
            is_running = False
        print("-" * 45)


    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == 'y':
        main()  
    else:
        print("=" * 50)
        print("               THANK YOU FOR PLAYING")
        print("=" * 50)

if __name__ == '__main__':
    main()
