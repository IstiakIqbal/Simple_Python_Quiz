import tkinter as tk
from tkinter import messagebox

def load_question():
    global question_number
    if question_number < len(questions):
        question = questions[question_number]
        label_question.config(text=question["question"])
        for idx, option in enumerate(question["options"]):
            buttons[idx].config(text=option)
    else:
        show_result()

def check_answer(index):
    global score
    correct_answer = questions[question_number]["answer"]
    selected_answer = chr(97 + index)
    if selected_answer == correct_answer:
        score += 5
        messagebox.showinfo("Correct", "Correct! You earned 5 points.")
    else:
        score -= 2
        messagebox.showerror("Incorrect", "Incorrect! You lost 2 points.")

def next_question():
    global question_number
    question_number += 1
    load_question()

def show_result():
    percentage = (score / (5 * len(questions))) * 100
    result_message = f"Your total score: {score}\nPercentage: {percentage:.2f}%"
    if percentage >= 60:
        result_message += "\nCongratulations! You passed the quiz!"
    else:
        result_message += "\nUnfortunately, you failed. Better luck next time!"
    messagebox.showinfo("Quiz Finished", result_message)
    root.quit()

root = tk.Tk()
root.title("Python Quiz")
root.geometry('600x400')

questions = [
    {"question": "What is the keyword to define a function in Python?",
     "options": ["a) func", "b) def", "c) function"], "answer": "b"},
    {"question": "What is the correct file extension for Python files?",
     "options": ["a) .py", "b) .pyt", "c) .txt"], "answer": "a"},
    {"question": "How do you insert comments in Python code?",
     "options": ["a) // comment", "b) /* comment */", "c) # comment"], "answer": "c"},
    {"question": "Which data type is immutable?",
     "options": ["a) list", "b) tuple", "c) dict"], "answer": "b"},
    {"question": "What is the output of 3**2 in Python?",
     "options": ["a) 6", "b) 9", "c) 8"], "answer": "b"},
    {"question": "What does the 'len()' function do?",
     "options": ["a) Finds the length", "b) Converts to a string", "c) Appends an element"], "answer": "a"},
    {"question": "Which operator is used for equality comparison?",
     "options": ["a) =", "b) ==", "c) !="], "answer": "b"},
    {"question": "Which keyword is used to create a loop in Python?",
     "options": ["a) repeat", "b) for", "c) loop"], "answer": "b"},
    {"question": "How do you start an 'if' statement in Python?",
     "options": ["a) if:", "b) if ():", "c) if {}:"], "answer": "a"},
    {"question": "What is the output of 'print(type(10))'?",
     "options": ["a) <class 'int'>", "b) <type 'int'>", "c) <data 'int'>"], "answer": "a"}
]

score = 0
question_number = 0

label_question = tk.Label(root, text="", font=("Arial", 14))
label_question.pack(pady=20)

buttons = []
for idx in range(3):
    button = tk.Button(root, text="", font=("Arial", 12), width=40,
                       command=lambda idx=idx: check_answer(idx))
    button.pack(pady=5)
    buttons.append(button)

next_button = tk.Button(root, text="Next", font=("Arial", 12), command=next_question)
next_button.pack(pady=20)

load_question()
root.mainloop()
