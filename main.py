questions = ("Where is Genshin Impact set?",
             "How many elements are there in the game?",
             "Which nation is based on Germany??",
             "Where does Chlorinde live?",
             "What is Sumeru famous for?",
             "What does the The Oratrice Mecanique d'Analyse Cardinale produce?",
             "What is the relationship between Jean and Barbara?",
             "How old is Yae Miko?",
             "What is the name of the Dendro dragon?",
             "What is Hutao's job?")
options = (("A. USA", "B. Tevyat", "C. Japan", "D. India"),
           ("A. 5", "B. 6", "C. 7", "D. 9"),
           ("A. Sumeru", "B. Natlan", "C. Liyue", "D. Mondstadt"),
           ("A. Inazuma", "B. Fontaine", "C. Sumeru", "D. Sneznaya"),
           ("A. Library", "B. Sages", "C. Desert", "D. Akademiya"),
           ("A. Indemnitium", "B. Anemonium", "C. Hydronium", "D. Dendrobium"),
           ("A. Rivals", "B. Siblings", "C. Friends", "D. Enemies"),
           ("A. 100 years", "B. 500 years", "C. 22 years", "D. 30 years"),
           ("A. Azdaha", "B. Dvalin", "C. Apep", "D. None of These"),
           ("A. Singer", "B. Poet", "C. Director", "D. Writer"))
answers = ("B", "C", "D", "B", "D", "A", "B", "B", "C", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ")
    guess = guess.upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("PAIMON says that the answer CORRECT!")
    else:
        print("PAIMON says that the answer is INCORRECT!")
        print(f"PAIMON says that {answers[question_num]} is the correct answer")
    question_num += 1

print("--------------------------")
print("         RESULTS!         ")
print("--------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
for guess in guesses:
    print(guess, end=" ")
print()
score = int(score / len(questions) * 100)
print(f"According to PAIMON your score is {score}%.")
