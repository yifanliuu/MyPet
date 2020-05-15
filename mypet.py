from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QToolTip
from PyQt5.QtCore import Qt, QPoint, QTimer
from PyQt5.QtGui import QFont, QCursor, QPixmap, QPainter, QPaintEvent
import random
import sys
import os
import time
from threading import Thread


class NewWindow(QWidget):
    def __init__(self, parent=None, **kwargs):
        self.i = 1
        super(NewWindow, self).__init__(parent)
        self.move(1200, 600)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.mypix()
        self.timer.start()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont("黑体", 14))
        y = ['hin', '在干嘛', '你猜']
        self.setToolTip(random.choice(y))
        time.sleep(1)

    def time_changed(self):
        self.i += 1
        t = Thread(target=self.mypix())
        t.start()
        t2 = Thread(target=self.initUI())
        t2.start()

    def mypix(self):
        self.pix = QPixmap('./img/shime1.png', '0', Qt.AvoidDither |
                           Qt.ThresholdAlphaDither | Qt.ThresholdDither)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.img = QLabel(self)
        self.img.setPixmap(self.pix)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = NewWindow()
    demo.show()
    sys.exit(app.exec_())
