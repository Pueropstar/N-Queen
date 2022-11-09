import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic   # ui 파일을 사용하기 위한 모듈 import
from secondwindow import secondwindow
#UI파일 연결 코드



UI_class = uic.loadUiType("main.ui")[0]
qnum=0
count =1
state={}
def Check(x,info): 
        for i in range (x): 
            if info[x] == info[i] or abs(info[x] - info[i]) == x - i: 
                return False 
        return True
  
def Dfs(x,info,N,count):
        
        if x == N:
          
            state[count]=tuple(info)
            count+=1
            return count

        for i in range(N): 
            info[x] = i
            if(Check(x,info)): 
                count=Dfs(x+1,info,N,count)
        
        return count


class MyWindow(QMainWindow, UI_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setInput()
        pixmap=QPixmap('퀸블랙.png')
        self.setWindowIcon(QIcon('퀸블랙.png'))
        self.label_2.setPixmap(pixmap)
        self.pushButton.clicked.connect(self.on_clicked)
        self.setFixedSize(QSize(754, 474))
        


    def on_clicked(self):
        inputqueen=self.inputtext.text()
        if(inputqueen==''):
            QMessageBox.information(self,'알림','퀸의 개수를 입력해주세요')
            return False
        inputNum=int(inputqueen)
        info = [0] * (inputNum)
        totalcount=Dfs(0,info,inputNum,count)
        self.hide()
        self.second=secondwindow(inputNum,totalcount-1,state)
        self.second.show()
        
    def setInput(self):
        re=QRegExp("[4-8]")
        font=QFont('NanumGothic',14)
        font.setBold(True)
        self.inputtext=QLineEdit(self)
        self.inputtext.setGeometry(350,390,31,41)
        self.inputtext.setFont(font)
        self.inputtext.setAlignment(Qt.AlignCenter)
        self.inputtext.setValidator(QRegExpValidator(re))
        
        

    

        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    Window = MyWindow() 
    Window.show()
    app.exec_()

