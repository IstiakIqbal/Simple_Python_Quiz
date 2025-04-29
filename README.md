# Python Quiz App

## Overview
The Python Quiz App is a simple, interactive quiz game built using Python and Tkinter. The app presents users with multiple-choice questions and gives feedback based on their answers. It also tracks the score and displays a result at the end of the quiz. This tool is a fun and engaging way to test your knowledge of Python basics.

## Key Features
- **Multiple-Choice Questions**: A set of questions with options, including Python-related topics.
- **Score Tracking**: The app keeps track of your score as you answer questions.
- **Correct/Incorrect Feedback**: Instant feedback is given after every question.
- **Result Display**: At the end, your score and percentage are displayed, along with a message on whether you passed or failed.
- **User-Friendly GUI**: Built with Tkinter, providing a simple and intuitive interface for users.

## Why Build a Quiz App?
- **Engaging Learning Tool**: This app makes learning and testing knowledge on Python fun and interactive.
- **Improved Python Skills**: The project helped me practice fundamental Python concepts such as functions, loops, and GUI design with Tkinter.
- **GUI Experience**: Gained hands-on experience in building user interfaces using Tkinter in Python.

## How It Works
1. **Question Display**: Users are shown a question with multiple-choice options.
2. **Answer Checking**: After selecting an answer, the app checks if it's correct and updates the score accordingly.
3. **Next Question**: After each answer, users click "Next" to move on to the next question.
4. **Result Calculation**: After the final question, the app calculates and displays the total score and percentage.

## Code Walkthrough
### Imports and Setup
```python
import tkinter as tk
from tkinter import messagebox


tkinter: Used to create the GUI.

messagebox: Displays message boxes for correct/incorrect answers and the result.

Main Functions
load_question(): Displays the current question and options.

check_answer(): Checks the user's answer and updates the score.

next_question(): Moves to the next question.

show_result(): Displays the user's score and a result message based on the percentage.

GUI Layout
python
Copy
Edit
root = tk.Tk()
root.title("Python Quiz")
root.geometry('600x400')
Initializes the main window with the title "Python Quiz" and a defined size.

Questions and Options
python
Copy
Edit
questions = [
    {"question": "What is the keyword to define a function in Python?", "options": ["a) func", "b) def", "c) function"], "answer": "b"},
    {"question": "What is the correct file extension for Python files?", "options": ["a) .py", "b) .pyt", "c) .txt"], "answer": "a"},
    # Add more questions here...
]
A list of dictionaries holding the questions, options, and correct answers.

Buttons and Labels
python
Copy
Edit
buttons = []
for idx in range(3):
    button = tk.Button(root, text="", font=("Arial", 12), width=40, command=lambda idx=idx: check_answer(idx))
    button.pack(pady=5)
    buttons.append(button)
Creates buttons dynamically based on the number of options for each question.

How to Run
Save the code: Copy the code above into a Python file, e.g., quiz_app.py.

Run the program:

bash
Copy
Edit
python quiz_app.py
Use the GUI:

Answer the questions by clicking on the options.

Click the Next button to proceed to the next question.

At the end of the quiz, your score and percentage will be displayed.

Example Scenarios
Scenario 1:
Question: What is the keyword to define a function in Python?

Answer: b) def

Score: +5 points

Scenario 2:
Question: What is the output of 3**2 in Python?

Answer: b) 9

Score: +5 points

## Screenshot
![Quiz App Screenshot](https://github.com/IstiakIqbal/Simple_Python_Quiz/blob/main/Simple%20Python%20Quiz.png?raw=true)
