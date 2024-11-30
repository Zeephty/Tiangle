import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt6.QtGui import QPainter, QColor
from random import randrange
from PyQt6 import uic

 
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 400, 400)
        self.setMouseTracking(True)

        uic.loadUi("UI.ui", self)
        
        self.pushButton.clicked.connect(self.toggle)

        self.b = False
    
    def toggle(self):
        self.b = True
        self.update()

    def paintEvent(self, event):
        if self.b:
            painter = QPainter(self)
            painter.setBrush(QColor("yellow"))
            randr = randrange(2, 300)
            painter.drawEllipse(randrange(0, self.width() - randr), randrange(0, self.height() - randr), randr, randr)
            self.b = False

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())