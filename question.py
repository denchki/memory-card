from main_window import (rbtn_1, rbtn_2, rbtn_3, rbtn_4, lb_question, lb_correct, box_radio_group, box_ans_group, btn_answer)
from random import shuffle

radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

class Question():
    def __init__(self, question, right_answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.right_answer = right_answer
        self.answers = [right_answer, wrong_answer1, wrong_answer2, wrong_answer3]

    def show(self):
        lb_question.setText(self.question)
        shuffle(self.answers)
        for i in range(len(radio_list)):
            radio_list[i].setText(self.answers[i])
            radio_list[i].setChecked(False)

    def check_result(self):
        selected_answer = ''
        for radio_button in radio_list:
            if radio_button.isChecked():
                selected_answer = radio_button.text()
        
        if selected_answer == self.right_answer:
            lb_correct.setText("Правильно")
        else:
            lb_correct.setText("Неправильно")
        show_result()

def show_result():
    box_radio_group.hide()
    box_ans_group.show()
    btn_answer.setText("Наступне питання")
    
questions = [
    Question("Машина", "cat", "carry", "kar", "Machine"),
    Question("Сонце", "sun", "sunstone", "stun", "stone"),
    Question("Окуляри", "Glasses", "glass", "grass", "koka kola"),
    Question("Телефон", "phone", "python", "pill", "pepsi"),
]
shuffle(questions)
current_question = 0

def show_question():
    global current_question
    if current_question < len(questions):
        questions[current_question].show()
    
    box_radio_group.show()
    box_ans_group.hide()
    btn_answer.setText("Відповісти")

def click_answer():
    global current_question
    if btn_answer.text() == "Відповісти":
        questions[current_question].check_result()
    else:
        current_question += 1
        if current_question < len(questions):
            show_question()
        else:
            lb_question.setText("Тест завершено!")
            btn_answer.setDisabled(True)
