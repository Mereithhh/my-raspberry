

import os, sys, time, json
from PyQt5.QtWidgets import (QApplication, QWidget,
	QLabel, QFrame, QPushButton, QStatusBar, 
	QHBoxLayout, QVBoxLayout, QLineEdit)
from PyQt5.QtGui import QFont, QPalette, QPixmap, QBrush, QIcon, QFontDatabase
from PyQt5.QtCore import QPoint, QSize, Qt, QCoreApplication, QBasicTimer
from bizhi import door

VERSION = "0.0.0"
UNIT = 1000
#MINSUNIT = 900
WEEK = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]


class MyButton(QPushButton):
	def __init__(self, father=None):  #path is a list
		super().__init__(father)

		
		self.setFocusPolicy(Qt.NoFocus)
		#self.setStyleSheet("QPushButton {background-color: transparent}")
		
		self.setFlat(True)


class Example(QWidget):
	hour = 'nnn'
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):

		#self.flush = 1 #初始化基本图像刷新值，由于首次启动程序背景图像从0开始，所以确保更新为下一张，从而直接从1开始

		
		self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗口标记，使其解除标题栏

		self.palette = QPalette()
		self.palette.setBrush(QPalette.Background, QBrush(QPixmap("/root/my-raspberry/show-info/icon/background/0.jpg")))
		self.setAutoFillBackground(True)  # 设置自动填充满背景图
		self.setPalette(self.palette)


		#imagehox = QHBoxLayout()
		#vox = QVBoxLayout()

		#self.btnclose = QPushButton()
		#self.btnclose.setFont(QFont("Arial",50))
		#self.btnclose.setGeometry(10, 100, 100, 100)

		self.lbltime = QLabel(self)
		self.lbltime.setFont(QFont("WenQuanYi Micro Hei",50))
		self.lbltime.setGeometry(35, 175, 700, 61)
		self.lbltime.setStyleSheet("QLabel {color: white}")

		
		self.lbldate = QLabel(self)
		self.lbldate.setFont(QFont("WenQuanYi Micro Hei", 25))
		self.lbldate.setGeometry(35, 250, 700, 41)
		self.lbldate.setStyleSheet("QLabel {color: white}")
		


		self.lblwordr = QLabel(self)
		self.lblwordr.setFont(QFont("WenQuanYi Micro Hei", 40))

		self.lblwordr.setGeometry(40, 80, 480, 120)
		self.lblwordr.setStyleSheet("QLabel {color: white; text-align: center;}")
      




	

		self.timer = QBasicTimer()
		self.timer.start(UNIT, self)

		
		
		#vox.addStretch(1)
		#vox.addWidget(self.lblwordr)
		
	
		

		#self.btnclose.clicked.connect(self.close)

		#self.setLayout(vox)
		self.setMinimumSize(480, 320)
		self.setMaximumSize(480, 320)
		self.move(0, 0)
		self.show()
		#self.showFullScreen()

	def timerEvent(self, *args, **kwargs):
		

		
		self.palette.setBrush(QPalette.Background, QBrush(QPixmap("/root/my-raspberry/show-info/icon/background/0.jpg")))


		localtime = list(time.localtime(time.time()))
		#year = localtime[0]
		mon = localtime[1]
		day = localtime[2]

		hour = localtime[3]
		if self.hour !=hour:
			door()
		self.hour = hour
		mins = localtime[4]
		sec = localtime[5]
		wday = localtime[6]

		#todo_list = SCHEDULE[WEEK[wday]]
    
		#todo = str()
		#for i in todo_list:
		#	todo += (i + ' ')
                
		try:
		    text = open('/root/my-raspberry/show-info/text.txt','r').readline()
		    self.lblwordr.setText(text)
		except:
			self.lblwordr.setText('')
		self.lbltime.setText("%02d:%02d:%02d" % (hour, mins,sec))
		self.lbldate.setText("%d,%d, %s" % (mon, day, WEEK[wday]))


if __name__ == '__main__':

	app = QApplication(sys.argv)
	app.setOverrideCursor(Qt.BlankCursor)  #when you put your cursor over the app,hide your cursor
	ex = Example()
	sys.exit(app.exec_())
