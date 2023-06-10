from PyQt5.QtCore import Qt
from random import shuffle
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QLabel,QPushButton, QButtonGroup
score = 0
class Question():
    def __init__(self, question, right, wrong1, wrong2, wrong3):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question("The state language of Brazil","Protuguese","English","Vietnamese","Brazilian"))
question_list.append(Question("How many presidents are there in the United States of America?","46","45","44","47"))
question_list.append(Question("3 + 3 x 3 = ?","12","9","15","18"))

app = QApplication([])
window = QWidget()
window.setWindowTitle("Memory Card")
window.resize(400,200)
question = QLabel("Which nationality does not exist?")
answer_bth = QPushButton("Answer")
answer_opt = QGroupBox("Answer options")
layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()
Ansbtn1 = QRadioButton("Enets")
Ansbtn2 = QRadioButton("Chulyms")
Ansbtn3 = QRadioButton("Smurfs")
Ansbtn4 = QRadioButton("Aleuts")
RadioBtn = QButtonGroup()
RadioBtn.addButton(Ansbtn1)
RadioBtn.addButton(Ansbtn2)
RadioBtn.addButton(Ansbtn3)
RadioBtn.addButton(Ansbtn4)
result = QGroupBox("Test result")
result1 = QLabel("Are you correct or not?")
correct = QLabel("Correct answer : Enets")
score_label = QLabel("Score : 0")
lay_res = QVBoxLayout()
lay_res.addWidget(result1)
lay_res.addWidget(score_label)
lay_res.addWidget(correct)
result.setLayout(lay_res)
layout2.addWidget(Ansbtn1)
layout2.addWidget(Ansbtn2)
layout3.addWidget(Ansbtn3)
layout3.addWidget(Ansbtn4)
layout1.addLayout(layout2)
layout1.addLayout(layout3)
answer_opt.setLayout(layout1)
layline1=QHBoxLayout()
layline2=QHBoxLayout()
layline3=QHBoxLayout()
layline1.addWidget(question)
layline2.addWidget(answer_opt)
layline2.addWidget(result)
result.hide()
layline3.addWidget(answer_bth)
laycard = QVBoxLayout()
laycard.addLayout(layline1)
laycard.addLayout(layline2)
laycard.addLayout(layline3)
window.setLayout(laycard)
window.cur_question = -1

def show_result():
    score_label.setText(f"Score : {str(score)}/3")
    answer_opt.hide()
    result.show()
    answer_bth.setText("Next question")
def show_question():
    answer_opt.show()
    result.hide()
    answer_bth.setText("Answer")
    RadioBtn.setExclusive(False)
    Ansbtn1.setChecked(False)
    Ansbtn2.setChecked(False)
    Ansbtn3.setChecked(False)
    Ansbtn4.setChecked(False)
    RadioBtn.setExclusive(True)
answerlist = [Ansbtn1,Ansbtn2,Ansbtn3,Ansbtn4]
def ask(q : Question):
    for i in range(5):
        shuffle(answerlist)
    answerlist[0].setText(q.right)
    answerlist[1].setText(q.wrong1)
    answerlist[2].setText(q.wrong2)
    answerlist[3].setText(q.wrong3)
    question.setText(q.question)
    correct.setText(f"Correct answer : {q.right}")
    show_question()
def start_test():
    if answer_bth.text() == "Answer":
        check_answer()
    else:
        next_question()
def show_correct(result2):
    result1.setText(result2)
    show_result()
def check_answer():
    global score
    if answerlist[0].isChecked():
        show_correct("Correct!")
        if score != 3:
            score += 1
    else:
        show_correct("Incorrect!")
def next_question():
    if window.cur_question == 2:
        window.cur_question -= 2
    else:
        window.cur_question += 1
    if window.cur_question >= len(question_list):
        show_result()
    else:
        q = question_list[window.cur_question]
        ask(q)
answer_bth.clicked.connect(start_test)
window.show()
app.exec_()