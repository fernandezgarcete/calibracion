# coding: utf-8
from calculo import leer, corregir, crear_archivo

__author__ = 'Juanjo'

import sys
from os.path import expanduser
from PyQt4.QtCore import *
from PyQt4.QtGui import QApplication, QWidget, QLabel,QPushButton, QVBoxLayout, QLineEdit, QGroupBox, QTextEdit, \
    QFileDialog, QIcon

class Calibrador(QWidget):
    def __init__(self, parent=None):
        super(Calibrador, self).__init__(parent)

        layout = QVBoxLayout()

        self.btabrir = QPushButton('Abrir')
        self.btabrir.clicked.connect(self.abrirArchivo)
        layout.addWidget(self.btabrir)

        self.gb1 = QGroupBox('Valores a Calibrar')
        l1 = QVBoxLayout()

        self.lx1 = QLabel('Archivo X1')
        self.x1 = QLineEdit()
        self.x1.setReadOnly(True)
        l1.addWidget(self.lx1)
        l1.addWidget(self.x1)

        self.lx2 = QLabel('Archivo X2')
        self.x2 = QLineEdit()
        self.x2.setReadOnly(True)
        l1.addWidget(self.lx2)
        l1.addWidget(self.x2)

        self.gb1.setLayout(l1)
        layout.addWidget(self.gb1)

        self.gb2 = QGroupBox('Valores de Referencia')
        l2 = QVBoxLayout()

        self.ly1 = QLabel('Archivo Y1')
        self.y1 = QLineEdit()
        self.y1.setReadOnly(True)
        l2.addWidget(self.ly1)
        l2.addWidget(self.y1)

        self.ly2 = QLabel('Archivo Y2')
        self.y2 = QLineEdit()
        self.y2.setReadOnly(True)
        l2.addWidget(self.ly2)
        l2.addWidget(self.y2)

        self.gb2.setLayout(l2)
        layout.addWidget(self.gb2)

        self.btlimpiar = QPushButton('Limpiar')
        self.btlimpiar.clicked.connect(self.limpiar)
        layout.addWidget(self.btlimpiar)

        self.contents = QTextEdit()
        self.contents.setReadOnly(True)
        layout.addWidget(self.contents)

        self.btcalibrar = QPushButton('Calibrar')
        self.btcalibrar.clicked.connect(self.calibrar)
        layout.addWidget(self.btcalibrar)

        self.setLayout(layout)
        self.setWindowTitle('Calibrador')
        self.setWindowIcon(QIcon('c:/Users/Juanjo/Pictures/CONAE_chico_transp.ico'))

    def abrirArchivo(self):
        f = QFileDialog.getOpenFileName(self, 'Abrir archivo', expanduser('~'), 'Textos (*.txt)')
        nom = f.split('/')
        if self.x1.text() == '':
            self.xi = f
            self.x1.setText(nom[len(nom)-1])
        elif self.x2.text() == '':
            self.xj = f
            self.x2.setText(nom[len(nom)-1])
        elif self.y1.text() == '':
            self.yi = f
            self.y1.setText(nom[len(nom)-1])
        elif self.y2.text() == '':
            self.yj = f
            self.y2.setText(nom[len(nom)-1])
        else:
            self.contents.setText('Limpie los campos para cagar nuevos archivos')

    def limpiar(self):
        self.x1.clear()
        self.x2.clear()
        self.y1.clear()
        self.y2.clear()
        self.contents.clear()

    def calibrar(self):
        if self.x1.text() == '' or self.x2.text() == '' or self.y1.text() == '' or self.y2.text() == '':
            self.contents.setText('Cargue todos los archivos antes de calibrar.')
        else:
            self.contents.setText('Calibrando...')
            w, xi, xj, yi, yj = leer(self.xi, self.xj, self.yi, self.yj)
            if isinstance(xi, list) and isinstance(xj, list) and isinstance(yi, list) and isinstance(yj, list):
                self.c1, self.c2 = corregir(w, xi, xj, yi, yj)
                crear_archivo(w, self.c1, self.c2, self.x1.text().split('.')[0], self.x2.text().split('.')[0])
                self.contents.setText('Completado.\nArchivos generados en el Escritorio.\n\n'
                                      'Se calibraron los archivos:\n'+self.x1.text()+'\n'+self.x2.text())
            else:
                if isinstance(xi, str):
                    self.contents.setText('Se encontró inconsistencia en los datos contenidos por el archivo: \n\n* '
                                          +self.x1.text()+'\n\n'+'Limpie los campos e ingrese nuevamente archivos '
                                          'con datos correctos de la forma:\n\nWavelength\tnombre_archivo\n350\t'
                                            '7,06635974347591E-03\n351\t7,32030812650919E-03\n...')
                if isinstance(xj, str):
                    self.contents.setText('* Se encontró inconsistencia en los datos contenidos por el archivo: \n\n* '
                                          +self.x2.text()+'\n\n'+'Limpie los campos e ingrese nuevamente archivos '
                                          'con datos correctos de la forma:\n\nWavelength\tnombre_archivo\n350\t'
                                            '7,06635974347591E-03\n351\t7,32030812650919E-03\n...')
                if isinstance(yi, str):
                    self.contents.setText('* Se encontró inconsistencia en los datos contenidos por el archivo: \n\n* '
                                          +self.y1.text()+'\n\n'+'Limpie los campos e ingrese nuevamente archivos '
                                          'con datos correctos de la forma:\n\nWavelength\tnombre_archivo\n350\t'
                                            '7,06635974347591E-03\n351\t7,32030812650919E-03\n...')
                if isinstance(yj, str):
                    self.contents.setText('* Se encontró inconsistencia en los datos contenidos por el archivo: \n\n* '
                                          +self.y2.text()+'\n\n'+'Limpie los campos e ingrese nuevamente archivos '
                                          'con datos correctos de la forma:\n\nWavelength\tnombre_archivo\n350\t'
                                            '7,06635974347591E-03\n351\t7,32030812650919E-03\n...')


def main():
    app = QApplication(sys.argv)
    ex = Calibrador()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
