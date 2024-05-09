from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QPushButton, QLabel, QVBoxLayout, QWidget,QLineEdit)
import sys
from random import randint
class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def update_label(self):
        self.label.setText("another  window %d " % randint(0,100))
class TheOtherWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()# 레이아웃을 수직(Vertical) 으로 정렬함
        self.label = QLabel()
        layout.addWidget(self.label) #레이아웃에 위젯(label) 추가
        self.setLayout(layout)#TheOtherWindow 에 layout 추가
    def update_label(self):
        self.label.setText("The other window %d " %randint(70,800))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cnt=0
        self.list2=[]
        self.w1 = AnotherWindow()  # No external window yet.
        self.w2 = TheOtherWindow()  # No external window yet.
        self.mainWidget= QWidget()
        self.mainLayout =QVBoxLayout(self.mainWidget)
        self.button = QPushButton("Push for Window")
        self.lineEdit = QLineEdit()
        self.mainLayout.addWidget(self.mainWidget)
        self.mainLayout.addWidget(self.button)
        self.mainLayout.addWidget(self.lineEdit)
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.mainWidget)
    def show_new_window(self, checked):
        self.cnt+=1
        print(self.cnt)
        self.list2.append(str(self.cnt))
        print(self.list2)
        if self.cnt%3==0:
            self.lineEdit.setText(str(self.cnt)) #리스트의 총합을 추가하는 코드로 변경
            self.w1.close()
            self.w2.update_label()#초기 라벨은 기본값이고 호출될때 라벨의 값을 변경함
            self.w2.show()
        else:
            self.w2.close()
            self.w1.update_label()
            self.w1.show()
app = QApplication(sys.argv)
w = MainWindow() #MainWindow객체 생성시 생성자에서 2개의 window 객체 생성
#멤버변수 cnt의 값이 3의 배수일 경우와 그렇지 않은 경우의 서로 다른 윈도우를 표시하고 다른
#윈도우는 종료함
w.show()
app.exec()