import math
import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLCDNumber


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('kamil_calc.ui', self)
        for i in self.buttonGroup_digits.buttons():
            i.clicked.connect(self.run)
        for i in self.buttonGroup_binary.buttons():
            i.clicked.connect(self.sp)
        self.btn_eq.clicked.connect(self.result)
        self.btn_clear.clicked.connect(self.delete)
        self.btn_dot.clicked.connect(self.dot)
        self.btn_square.clicked.connect(self.spongeBob)
        self.btn_sqrt.clicked.connect(self.koren)
        self.btn_pi.clicked.connect(self.Pi)
        self.btn_fact.clicked.connect(self.factish)
        self.btn_sin.clicked.connect(self.sinus)
        self.btn_cos.clicked.connect(self.cosinus)
        self.btn_cos_2.clicked.connect(self.logorifm)
        self.btn_graph.clicked.connect(self.grafic)
        self.btn_delet.clicked.connect(self.aaaaa)


        self.text = '0'
        self.fr = ''
        self.table.setDigitCount(12)
        self.istouch = False

    def run(self):
        if not self.istouch:
            self.text += self.sender().text()
            self.fr += self.sender().text()
        else:
            self.text = self.sender().text()
            self.fr += self.sender().text()
            self.istouch = False
        if self.text[0] == 0:
            self.text = self.text[1:]
        self.table.display(float(self.text))

    def sp(self):
        self.fr += self.sender().text().replace('^', '**')
        self.istouch = True

    def result(self):
        try:
            self.text = str(eval(self.fr))
            self.table.display(float(self.text))
            self.fr = str(eval(self.fr))
        except Exception:
            self.table.display('Errorr')

    def delet(self):
        pass

    def spongeBob(self):
        self.fr += self.sender().text().replace('^', '**')
        self.result()

    def Pi(self):
        self.fr += str(math.pi)
        self.text += str(math.pi)
        self.result()

    def factish(self):
        try:
            self.fr = str(math.factorial(int(eval(self.fr))))
            self.text = str(math.factorial(int(self.text)))
            self.result()
        except Exception:
            self.table.display('Errorr')

    def sinus(self):
        try:
            self.fr = str(math.sin(int(eval(self.fr))))
            self.text = str(math.sin(int(self.text)))
            self.result()
        except Exception:
            self.table.display('Errorr')

    def cosinus(self):
        try:
            self.fr = str(math.cos(int(eval(self.fr))))
            self.text = str(math.cos(int(self.text)))
            self.result()
        except Exception:
            self.table.display('Errorr')

    def logorifm(self):
        try:
            self.fr = str(math.log(int(eval(self.fr))))
            self.text = str(math.log(int(self.text)))
            self.result()
        except Exception:
            self.table.display('Errorr')

    def aaaaa(self):
        self.fr = self.fr[:-1]
        self.text = self.text[:-1]
        if not self.text:
            self.text = '0'
        self.table.display(self.text)

    def koren(self):
        self.fr += '**0.5'
        self.result()

    def delete(self):
        self.text = '0'
        self.fr = ''
        self.istouch = False
        self.table.display('0')

    def dot(self):
        if self.fr:
            if self.fr[-1].isdigit():
                self.fr += '.'
                self.text += '.'
                if self.text[0] == '0':
                    self.text = self.text[1:]
        self.table.display(self.text)

    def grafic(self):
        self.g = Grafick()
        self.g.show()
        self.close()


class Grafick(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('kamil_graph.ui', self)
        self.btn_back.clicked.connect(self.calc)
        self.btn_clean.clicked.connect(self.cleaning)
        self.itog.clicked.connect(self.run)
    def calc(self):
        self.g = MyWidget()
        self.g.show()
        self.close()

    def cleaning(self):
        self.widget.clear()
    def run(self):
        ln = self.ln.text()
        x = np.linspace(-5, 5, 100)
        if 'sin' in ln:
            ln = ln.replace('sin', 'np.sin')
        if 'cos' in ln:
            ln = ln.replace('cos', 'np.cos')
        if 'log' in ln:
            ln = ln.replace('log', 'np.log')
        y = eval(ln)
        self.widget.plot(x, y)
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

