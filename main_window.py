from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])

btn_menu = QPushButton("Меню")
btn_sleep = QPushButton("Відпочити")
box_minutes = QSpinBox()
box_minutes.setValue(30)
lb_minutes = QLabel("хвилин")
lb_question = QLabel("")
btn_answer = QPushButton("Відповісти")

box_radio_group = QGroupBox("Варіанти відповідей")
radio_group = QButtonGroup()

rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

radio_group.addButton(rbtn_1)
radio_group.addButton(rbtn_2)
radio_group.addButton(rbtn_3)
radio_group.addButton(rbtn_4)

box_ans_group = QGroupBox('Результат тесту')
lb_result = QLabel('')
lb_correct = QLabel('')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

box_radio_group.setLayout(layout_ans1)

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment=Qt.AlignCenter)
box_ans_group.setLayout(layout_res)
box_ans_group.hide()

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_sleep)
layout_line1.addWidget(box_minutes)
layout_line1.addWidget(lb_minutes)

layout_line2.addWidget(lb_question, alignment = Qt.AlignCenter)

layout_line3.addWidget(box_radio_group)
layout_line3.addWidget(box_ans_group)

layout_line4.addWidget(btn_answer, alignment = Qt.AlignCenter)

layout_main = QVBoxLayout()

layout_main.addLayout(layout_line1, stretch=1)
layout_main.addLayout(layout_line2, stretch=2)
layout_main.addLayout(layout_line3, stretch=8)
layout_main.addStretch(1)
layout_main.addLayout(layout_line4)
layout_main.addStretch(1)
layout_main.addSpacing(5)
