__author__ = 'Vinita Pereira'
from PyQt4 import QtCore, QtGui, uic
from tkinter import *
import tkinter as tk
from tkinter.colorchooser import *

draw = uic.loadUiType("paint.ui")[0]

class paintwindows(QtGui.QDialog, draw):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.pallet.setStyleSheet("background-image: url(images/pallet.png);")
        self.paste.setStyleSheet("background-image: url(images/paste.jpg);")
        self.cut.setStyleSheet("background-image: url(images/cut.jpg);")
        self.copy.setStyleSheet("background-image: url(images/copy.jpg);")
        self.eraser.setStyleSheet("background-image: url(images/eraser.jpg);")
        self.brush.setStyleSheet("background-image: url(images/brush.jpg);")
        self.colorpicker.setStyleSheet("background-image: url(images/colorpicker.jpg);")
        self.select.setStyleSheet("background-image: url(images/select.png);")
        self.magnifier.setStyleSheet("background-image: url(images/magnifier.png);")
        self.crop.setStyleSheet("background-image: url(images/crop.png);")
        self.pencil.setStyleSheet("background-image: url(images/pencil.png);")
        self.resize.setStyleSheet("background-image: url(images/resize.png);")
        self.rotate.setStyleSheet("background-image: url(images/rotate.png);")
        self.fillcolor.setStyleSheet("background-image: url(images/fill.png);")
        self.text.setStyleSheet("background-image: url(images/a.png);")
        self.shapes.setStyleSheet("background-image: url(images/shapes.jpg);")
        self.pallet.clicked.connect(self.pallet_clicked)
        self.shapes.clicked.connect(self.shapes_clicked)
        self.size()


    def pallet_clicked(self):
        color = askcolor()
        self.pallet.configure(color)

    def shapes_clicked(self):
        shape = uic.loadUiType("cal.ui")[0]
        class calc(QtGui.QDialog, shape):
            def __init__(self, parent = None):
                QtGui.QDialog.__init__(self, parent)
                self.setupUi(self)
                self.oval.setStyleSheet("background-image: url(images/shapes/oval.png);")
                self.line.setStyleSheet("background-image: url(images/shapes/line.jpg);")
                self.curve.setStyleSheet("background-image: url(images/shapes/curve.jpg);")
                self.rectangle.setStyleSheet("background-image: url(images/shapes/rectangle.png);")
                self.roundedrectangle.setStyleSheet("background-image: url(images/shapes/roundedrectangle.png);")
                self.polygon.setStyleSheet("background-image: url(images/shapes/polygon.png);")
                self.triangle.setStyleSheet("background-image: url(images/shapes/triangle.png);")
                self.rttriangle.setStyleSheet("background-image: url(images/shapes/rttriangle.png);")
                self.diamond.setStyleSheet("background-image: url(images/shapes/diamond.png);")
                self.pentagon.setStyleSheet("background-image: url(images/shapes/pentagon.png);")
                self.hexagon.setStyleSheet("background-image: url(images/shapes/hexagon.jpg);")
                self.rtarrow.setStyleSheet("background-image: url(images/shapes/rtarrow.png);")
                self.ltarrow.setStyleSheet("background-image: url(images/shapes/ltarrow.png);")
                self.uparrow.setStyleSheet("background-image: url(images/shapes/uparrow.png);")
                self.downarrow.setStyleSheet("background-image: url(images/shapes/downarrow.png);")
                self.pt4star.setStyleSheet("background-image: url(images/shapes/pt4star.png);")
                self.pt5star.setStyleSheet("background-image: url(images/shapes/pt5star.png);")
                self.pt6star.setStyleSheet("background-image: url(images/shapes/pt6star.png);")
                self.rectcallout.setStyleSheet("background-image: url(images/shapes/rectcallout.png);")
                self.ovalcallout.setStyleSheet("background-image: url(images/shapes/ovalcallout.png);")
                self.cloudcallout.setStyleSheet("background-image: url(images/shapes/cloudcallout.png);")
                self.heart.setStyleSheet("background-image: url(images/shapes/heart.png);")
                self.lightening.setStyleSheet("background-image: url(images/shapes/lightening.jpg);")
                self.size()
        calc = calc(None)
        calc.show()
        calc.exec_()


app = QtGui.QApplication(sys.argv)
paintwindows = paintwindows(None)
paintwindows.show()
app.exec_()