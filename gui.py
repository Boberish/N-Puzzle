
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QAction, QLineEdit, QMessageBox, QInputDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from puzzleGen import puzzleGenerator
from parser import init, doit

#######globals:
heuristicChoice = ''
sizeChoice = 0

# # Choose The size of the puzzle
class SizePuzz(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'N Puzzle size Choice'
        self.left = 1000
        self.top = 500
        self.width = 640
        self.height = 480
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Box for the integer
        self.getInteger()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.show()
 
    def getInteger(self):
        i, okPressed = QInputDialog.getInt(self, "Get integer","Define the size of a column:", 3, 3, 9, 1)
        if okPressed:
            sizeChoice = int(i)
            print(i)
            # make that a tuple of tuple
            puzzleList = puzzleGenerator(sizeChoice)
            print(puzzleList)
            startFromGui(sizeChoice, puzzleList)
            self.close()

# Choose of the Heuristic
class App(QDialog):
 
    def __init__(self):
        super().__init__()
        self.title = 'N Puzzle heuristic Choice'
        self.left = 1000
        self.top = 500
        self.width = 640
        self.height = 480
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # self.statusBar().showMessage('Welcome !')

        # Horizontal Layout to align buttons
        self.createHorizontalLayout()
 
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
 
        label = QLabel("Which Heuristic do you want to use?", self)
        label.resize(500, 50)
        label.move(200,150)

        self.show()
 
    def createHorizontalLayout(self):
        self.horizontalGroupBox = QGroupBox("")
        layout = QHBoxLayout()

        # first button : Manhattan
        manhattanButton = QPushButton('Manhattan Distance', self)
        manhattanButton.clicked.connect(self.on_click_manhattan)
        layout.addWidget(manhattanButton)

        # second Button: Not in place box
        notInPlaceButton = QPushButton('Not in Place', self)
        notInPlaceButton.clicked.connect(self.on_click_notInPlace)
        layout.addWidget(notInPlaceButton)

        # Tird Button: n-MaxSwap ou Gushing
        maxSwapButton = QPushButton('n-MaxSwap', self)
        maxSwapButton.clicked.connect(self.on_click_gusching)
        layout.addWidget(maxSwapButton)

        self.horizontalGroupBox.setLayout(layout)
 
    @pyqtSlot()
    def on_click_manhattan(self):
        print('Manhattan choosen')
        heuristicChoice = 'md'
        self.accept()
    def on_click_notInPlace(self):
        print('Not in place choosen')
        heuristicChoice = 'np'
        self.accept()
    def on_click_gusching(self):
        print('n-MaxSwap ou Gushing choosen')
        heuristicChoice = 'gt'
        self.accept()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    sizePuzz = SizePuzz()
    ex = App()
    sys.exit(app.exec_())



def startFromGui(size, start):
    init(start)
    doit(start)















# import sys
# import random
# from PySide2 import QtWidgets, QtGui
# from PySide2.QtCore import *
# import numpy as np

# class MyScene(QtWidgets.QGraphicsScene):
#     def __init__(self, s, grids):
#         QtWidgets.QGraphicsScene.__init__(self)
#         self.grids = grids
#         self.s = s
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.display_next)
#         self.timer.start(500)
#         self.display_next()
#     def display_all(self):
#         for grid in self.grids:
#             display(self.s, grid, self)
#     def display_next(self):
#         if self.grids:
#             curr = self.grids.pop(0)
#             self.display(curr)
#         else:
#             self.timer.stop()
#     def display(self, grid):
#         self.clear()
#         for y in range(self.s):
#             for x in range(self.s):
#                 if grid[x][y] != 0:
#                     self.addText("{}".format(grid[x][y])).setPos(y * 100, x * 100)
#                     self.addRect(y * 100, x * 100, 100, 100)

# def display_all(s, grids):
#     grids = [np.asarray(g).reshape(s,s) for g in grids]
#     app = QtWidgets.QApplication([])
#     scene = MyScene(s, grids)
#     view = QtWidgets.QGraphicsView(scene)
#     view.resize(800, 800)
#     view.show()
#     sys.exit(app.exec_())