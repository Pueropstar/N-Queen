import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic   # ui 파일을 사용하기 위한 모듈 import

#UI파일 연결 코드

form_secondwindow = uic.loadUiType("sub.ui")[0]

class secondwindow(QMainWindow, form_secondwindow) :
    
    def __init__(self,qnum,totalcount,state) :
        super().__init__()
        self.state=state
        self.qnum=qnum
        self.totalCase=totalcount
        self.currentpage=1
        self.pixmap=QPixmap("퀸블랙.png")
        self.font=QFont('NanumGothic',16)
        self.font.setBold(True)
        self.setFixedSize(QSize(1000, 750))
        self.setupUi(self)
        self.setWindowIcon(QIcon('퀸블랙.png'))
        self.setWindowTitle(f"{self.qnum} Queen")
        self.init_gridlayout()
        self.init_button()
        self.show_page(self.currentpage)
        self.setQueen(self.state,self.currentpage)

        
        
    def init_gridlayout(self):
                
        widget=QWidget(self)
        
        
        gridLayout=self.chessLayout
        gridLayout.setSpacing(0)
        gridLayout.setVerticalSpacing(0)
        
        numberRowLay=self.numberRowLayout
        numberColLay=self.numberColLayout
        
        for i in range(self.qnum):

            text=QLabel()
            text1=QLabel()
            text.setFont(self.font)
            text1.setFont(self.font)
            text.setText(f"{i}")
            text1.setText(f"{i}")
            text.setAlignment(Qt.AlignCenter)
            text1.setAlignment(Qt.AlignCenter)            
            numberRowLay.addWidget(text,i,0)
            numberColLay.addWidget(text1,0,i)

            for j in range(self.qnum):

                board=QLabel()
                board.setAlignment(Qt.AlignCenter)

                if(i%2!=0):
                    
                    if(j%2==0):
                        board.setStyleSheet("background-color:grey;"
                                            "border:1px solid black;")
                        gridLayout.addWidget(board,i,j,1,1)
                   
                    else:
                        
                        board.setStyleSheet("background-color:white;"
                                            "border:1px solid black;")
                        gridLayout.addWidget(board,i,j,1,1)
                else:
                    if(j%2==0):
                        board.setStyleSheet("background-color:white;"
                                            "border:1px solid black;")
                        gridLayout.addWidget(board,i,j,1,1)
                     
                    else:
                        board.setStyleSheet("background-color:grey;"
                                            "border:1px solid black;")
                        gridLayout.addWidget(board,i,j,1,1)
        self.setCentralWidget(widget)
    
    def init_button(self):
        
        
        RButton=QPushButton(self)
        LButton=QPushButton(self)

        RButton.setFont(self.font)
        LButton.setFont(self.font)
        
        RButton.setText('>')
        LButton.setText('<')
        
        LButton.setGeometry(300,675,81,41)
        RButton.setGeometry(590,675,81,41)
        
        RButton.clicked.connect(self.btn_RClick)
        LButton.clicked.connect(self.btn_LClick)
        
    def show_page(self,current:int):
        self.page.setText(f'{current} / {self.totalCase}')
            
        
    def btn_RClick(self):
        if(self.currentpage==self.totalCase):
            QMessageBox.information(self,"알림","마지막 페이지입니다")
            return False
        else:
            save=self.currentpage
            self.initQueen(self.state,save)
            self.currentpage+=1
            self.setQueen(self.state,self.currentpage)
            self.show_page(self.currentpage)
        
        
    def btn_LClick(self):
        if(self.currentpage==1):
            QMessageBox.information(self,"알림","마지막 페이지입니다")
            return False
        else:
            save=self.currentpage
            self.initQueen(self.state,save)
            self.currentpage-=1
            self.setQueen(self.state,self.currentpage)
            self.show_page(self.currentpage)
            
        
    def setQueen(self,state,current):
        pixmap1=self.pixmap.scaled(450/self.qnum,450/self.qnum,Qt.KeepAspectRatio)
        qInfo=state[current]
        chessBoard=self.chessLayout
        for i in range(self.qnum):
            queenPos=chessBoard.itemAtPosition(i,qInfo[i]).widget()
            queenPos.setPixmap(pixmap1)
            
    
    def initQueen(self,state,current):
        pixmap=QPixmap()
        qInfo=state[current]
        chessBoard=self.chessLayout
        for i in range(self.qnum):
            queenPos=chessBoard.itemAtPosition(i,qInfo[i]).widget()
            queenPos.setPixmap(pixmap)


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    Window = secondwindow() 
    Window.show()   
    app.exec_()
