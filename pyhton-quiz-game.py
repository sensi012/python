# Python quiz game

questions = ("How many elements are in the periodic table?: ",
"what is the first Alphabet?: ",
"what is the last Alphabet?: ",
"what is the name of the hottest planet?: ",
"How many moon, does the earth have?: ",
)


options = (("A. 116", "B. 117", "C. 118", "D. 119"), 
("A. D", "B. E", "C. F", "D. A"), 
("A. Z", "B. W", "C. G", "D. K"), 
("A. Earth", "B. Moon", "C. Saturn", "D. Mercury"), 
("A. 1", "B. 2", "C. 3", "D. 4"))

answers = ("C", "D", "A", "A", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1


################################################
# dictionaries
################################################
capitals = {"USA": "Washington D.C",
"India": "New Dehli", 
"Russia": "Moscow"
}

print(dir(capitals))