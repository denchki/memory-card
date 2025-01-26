from PyQt5.QtWidgets import *

lb_question = QLabel("Введіть запитання:")
le_question = QLineEdit()
le_question.setFixedWidth(300)

lb_correct = QLabel("Введіть вірну відповідь:")
le_correct = QLineEdit()
le_correct.setFixedWidth(300)

lb_wrong1 = QLabel("Введіть першу хибну відповідь:")
le_wrong1 = QLineEdit()
le_wrong1.setFixedWidth(300)

lb_wrong2 = QLabel("Введіть другу хибну відповідь:")
le_wrong2 = QLineEdit()
le_wrong2.setFixedWidth(300)

lb_wrong3 = QLabel("Введіть третю хибну відповідь:")
le_wrong3 = QLineEdit()
le_wrong3.setFixedWidth(300)

btn_add = QPushButton("Додати запитання")
btn_clear = QPushButton("Очистити")
btn_back = QPushButton("Назад")

layout_1 = QHBoxLayout()
layout_2 = QHBoxLayout()
layout_3 = QHBoxLayout()
layout_4 = QHBoxLayout()
layout_5 = QHBoxLayout()

layout_1.addWidget(lb_question)
layout_1.addWidget(le_question)

layout_2.addWidget(lb_correct)
layout_2.addWidget(le_correct)

layout_3.addWidget(lb_wrong1)
layout_3.addWidget(le_wrong1)

layout_4.addWidget(lb_wrong2)
layout_4.addWidget(le_wrong2)

layout_5.addWidget(lb_wrong3)
layout_5.addWidget(le_wrong3)

layout_6 = QHBoxLayout()
layout_7 = QHBoxLayout()

layout_6.addWidget(btn_add)
layout_6.addWidget(btn_clear)

layout_7.addWidget(btn_back)

layout_main = QVBoxLayout()

layout_main.addLayout(layout_1)
layout_main.addLayout(layout_2)
layout_main.addLayout(layout_3)
layout_main.addLayout(layout_4)
layout_main.addLayout(layout_5)
layout_main.addLayout(layout_6)
layout_main.addLayout(layout_7)