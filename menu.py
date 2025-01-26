from PyQt5.QtWidgets import *
from menu_window import (le_correct, le_question, le_wrong1, le_wrong2, le_wrong3, btn_clear, btn_back, btn_add, layout_main)
from question import questions, Question
from random import shuffle

win_menu = QWidget()
win_menu.setWindowTitle("Menu")
win_menu.setLayout(layout_main)

def clear():
    le_correct.clear()
    le_question.clear()
    le_wrong1.clear()
    le_wrong2.clear()
    le_wrong3.clear()

def back():
    win_menu.close()

def add_question():
    question_text = le_question.text()
    correct_answer = le_correct.text()
    wrong_1 = le_wrong1.text()
    wrong_2 = le_wrong2.text()
    wrong_3 = le_wrong3.text()

    questions.append(Question(question_text, correct_answer, wrong_1, wrong_2, wrong_3))
    shuffle(questions)
    clear()

btn_clear.clicked.connect(clear)
btn_back.clicked.connect(back)
btn_add.clicked.connect(add_question)