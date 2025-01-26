from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from main_window import app, layout_main, btn_answer, btn_menu, btn_sleep, box_minutes
from question import show_question, click_answer
from menu import win_menu

win = QWidget()
win.resize(600, 500)
win.move(300, 300)
win.setWindowTitle("Memory Card")
win.setLayout(layout_main)

def restore_window():
    win.showNormal()
    win.raise_()

def sleep():
    minutes = box_minutes.value()
    win.showMinimized()
    QTimer.singleShot(1000 * 60 * minutes, restore_window)

def show_menu():
    win_menu.show()

btn_menu.clicked.connect(show_menu)
btn_answer.clicked.connect(click_answer)
btn_sleep.clicked.connect(sleep)

show_question()

win.show()
app.exec_()