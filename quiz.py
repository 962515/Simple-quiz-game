print("******************************************************************")
print("Welcome to my quiz game!!")

score = 0

question_bank = [
    {"text": "Who developed the Python language?", "answer": "B"},
    {"text": "In which language is Python written?", "answer": "C"},
    {"text": "Which one of the following is the correct extension of the Python file?", "answer": "A"},
    {"text": "In which year was the Python 3.0 version developed?", "answer": "A"},
    {"text": "What do we use to define a block of code in Python language?", "answer": "C"},
    {"text": "Why does the name of local variables start with an underscore discouraged?", "answer": "C"},
]


option = [
    ["A. Zim Den", "B. Guido van Rossum", "C. Niene Stom", "D. Wick van Rossum"],
    ["A. English", "B. PHP", "C. C", "D. All of the above"]
    ["A. PY", "B. Python", "C. p", "D. None of these"],
    ["A. 2008", "B. 2000", "C. 2003", "D. 2005"],
    ["A. key", "B. Bracket", "C. indentation", "D. none of these"],
    ["A. To identify the variable", "B. It confuses the interpreter", "C. It indicates a private variable of a class", "D. none of these"],
]

def check_answer(user_ans, correct_answer):
    return user_ans == correct_answer

for question_number in range(len(question_bank)):
    print(question_bank[question_number]["text"])
    for i in option[question_number]:
        print(i)

    ans = input("Enter the answer (A/B/C/D): ").upper()
    is_correct = check_answer(ans, question_bank[question_number]["answer"])
    if is_correct:
        print("Correct answer!")
        score += 1
    else:
        print("Wrong answer!")
        print(f"The correct answer is: {question_bank[question_number]['answer']}")
       
        explanations = [
            "Guido van Rossum is the creator of the Python programming language.",
            "Python is written in C, which makes it an interpreted language.",
            "The correct extension for Python files is .py.",
            "Python 3.0, also known as Python 3000 and Py3k, was released in 2008.",
            "Indentation is used to define a block of code in Python.",
            "Local variables starting with an underscore indicates a private variable of a class."
        ]
        print(f"Explanation: {explanations[question_number]}")

print("*********************************************************************************************************")
print(f"The final score is {score}")
print(f"Your score is {(score / len(question_bank))*100}%")
