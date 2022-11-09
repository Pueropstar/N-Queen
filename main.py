import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic   # ui 파일을 사용하기 위한 모듈 import
from secondwindow import secondwindow
#UI파일 연결 코드

UI_class = uic.loadUiType("main.ui")[0]

class MyWindow(QMainWindow, UI_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(QSize(754, 474))
        self.setWindowIcon(QIcon('퀸블랙.png'))
        self.setInput()
        self.count =1
        self.state={}
        self.pixmap=QPixmap('퀸블랙.png')
        self.label_2.setPixmap(self.pixmap)
        self.pushButton.clicked.connect(self.on_clicked)

    def on_clicked(self):

        blankInput=self.inputtext.text()
        if(blankInput==''):

            QMessageBox.information(self,'알림','퀸의 개수를 입력해주세요')
            return False

        queenNum=int(blankInput)
        queenInfo = [0] * queenNum
        totalcount=self.Dfs(0,queenInfo,queenNum,self.count)-1
        self.showSecondWnd(queenNum,totalcount,self.state)
        

    def showSecondWnd(self,queenNum,totalcount,state):
        self.hide()
        self.second=secondwindow(queenNum,totalcount,state)
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

    def Check(self,x,info): 
        for i in range (x): 
            if info[x] == info[i] or abs(info[x] - info[i]) == x - i: 
                return False 
        return True
  
    def Dfs(self,x,info,N,count):
        
        if x == N:
          
            self.state[count]=tuple(info)
            count+=1
            return count

        for i in range(N): 
            info[x] = i
            if(self.Check(x,info)): 
                count=self.Dfs(x+1,info,N,count)
        
        return count
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    Window = MyWindow() 
    Window.show()
    app.exec_()

