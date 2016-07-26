from calibrar import Calibrador
from grafico import Grafico

__author__ = 'Juanjo'
import sys
from PyQt4.QtGui import QMainWindow, QApplication

class MultiWin(QMainWindow):
    def __init__(self, parent=None):
        super(MultiWin, self).__init__(parent)
        self.winList = []

    def addwin(self, win):
        self.winList.append(win)


def main():
    app = QApplication(sys.argv)
    ex = MultiWin()
    ex.addwin(Calibrador)
    ex.addwin(Grafico)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
