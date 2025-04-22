questions = (
    "1. What is the capital of France?",
    "2. Which element has the chemical symbol 'O'?",
    "3. Who wrote 'Romeo and Juliet'?",
    "4. What is the largest planet in our solar system?",
    "5. Which language is primarily spoken in Brazil?",
    "6. What year did World War II end?",
    "7. Which organ pumps blood throughout the body?",
    "8. What is 9 x 7?",
    "9. Who painted the Mona Lisa?",
    "10. Which continent is the Sahara Desert in?"
)

options = (
    ("A. London", "B. Madrid", "C. Berlin", "D. Paris", "E. Rome"),
    ("A. Gold", "B. Oxygen", "C. Iron", "D. Hydrogen", "E. Carbon"),
    ("A. Charles Dickens", "B. William Wordsworth", "C. William Shakespeare", "D. Jane Austen", "E. Mark Twain"),
    ("A. Earth", "B. Saturn", "C. Jupiter", "D. Mars", "E. Venus"),
    ("A. Spanish", "B. Portuguese", "C. French", "D. English", "E. Italian"),
    ("A. 1939", "B. 1941", "C. 1945", "D. 1950", "E. 1963"),
    ("A. Brain", "B. Lungs", "C. Heart", "D. Kidney", "E. Liver"),
    ("A. 56", "B. 63", "C. 72", "D. 81", "E. 90"),
    ("A. Picasso", "B. Michelangelo", "C. Da Vinci", "D. Van Gogh", "E. Monet"),
    ("A. Asia", "B. Africa", "C. Europe", "D. South America", "E. Australia")
)

answers = ("D", "B", "C", "C", "B", "C", "C", "B", "C", "B")

guesses = []
score = 0
question_number = 0

print("=" * 50)
print("                 GENERAL QUIZ                 ")
print("=" * 50)

for question in questions:
    print(f"\n{question}")
    for option in options[question_number]:
        print(f"   {option}")

    guess = input("Your answer (A, B, C, D, E): ").upper()
    guesses.append(guess)

    if guess == answers[question_number]:
        score = score + 1
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer was: {answers[question_number]}")

    question_number = question_number + 1

print("\n" + "=" * 50)
print("                   RESULTS                    ")
print("=" * 50)

print("\nCorrect Answers:  ", end="")
for answer in answers:
    print(answer, end="  ")

print("\nYour Answers:     ", end="")
for guess in guesses:
    print(guess, end="  ")

percentage = int(score / len(questions) * 100)
print(f"\n\nYour final score: {score} / {len(questions)} ({percentage}%)")
print("=" * 50)
print("           Thank you for playing!             ")
print("=" * 50)