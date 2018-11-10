import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QAction, QLineEdit, QMessageBox, QInputDialog, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from puzzleGen import puzzleGenerator
from displayResult import * 
# from parser import init, doit

# globals: #
heuristicChoice = ''
# CHANGE THAT
sizeChoice = 3
puzzleList = []
# CHANGE THAT
retPath = [((1, 2, 3), (8, 0, 4), (7, 6, 5)), ((1, 2, 3), (0, 8, 4), (7, 6, 5)), ((0, 2, 3), (1, 8, 4), (7, 6, 5)), ((2, 0, 3), (1, 8, 4), (7, 6, 5)), ((2, 8, 3), (1, 0, 4), (7, 6, 5)), ((2, 8, 3), (1, 6, 4), (7, 0, 5)), ((2, 8, 3), (1, 6, 4), (0, 7, 5)), ((2, 8, 3), (0, 6, 4), (1, 7, 5)), ((2, 8, 3), (6, 0, 4), (1, 7, 5)), ((2, 8, 3), (6, 4, 0), (1, 7, 5)), ((2, 8, 3), (6, 4, 5), (1, 7, 0)), ((2, 8, 3), (6, 4, 5), (1, 0, 7)), ((2, 8, 3), (6, 4, 5), (0, 1, 7)),((2, 8, 3), (0, 4, 5), (6, 1, 7)), ((2, 8, 3), (4, 0, 5), (6, 1, 7)), ((2, 8, 3), (4, 5, 0), (6, 1, 7)), ((2, 8, 0), (4, 5, 3), (6, 1, 7)), ((2, 0, 8), (4, 5, 3), (6, 1, 7)), ((0, 2, 8), (4, 5, 3), (6, 1, 7)), ((4, 2, 8), (0, 5, 3), (6, 1, 7)), ((4, 2, 8), (5, 0, 3), (6, 1, 7)), ((4, 2, 8), (5, 3, 0), (6, 1, 7)), ((4, 2, 0), (5, 3, 8), (6, 1, 7)), ((4, 0, 2), (5, 3, 8), (6, 1, 7)), ((0, 4, 2), (5, 3, 8), (6, 1, 7)), ((5, 4, 2), (0, 3, 8), (6, 1, 7)), ((5, 4, 2), (3, 0, 8), (6, 1, 7)), ((5, 4, 2), (3, 1, 8), (6, 0, 7)), ((5, 4, 2), (3, 1, 8), (0, 6, 7))]


# Printing the Path step by step #
class DisplayPath(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'N Puzzle - Result Step By Step'
        self.left = 1000
        self.top = 500
        # self.width = 640
        # self.height = 480
        self.width = 200 * sizeChoice
        self.height = 120 * sizeChoice
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you want to go Step by Step ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # if buttonReply == QMessageBox.Yes:
        #     print('Yes clicked.')
        # else:
        #     print('No clicked.')

        # Creation of the table
        self.createTable()
 
        # Add box layout, add table to box layout and add box layout to widget #
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 
 
        # Show widget #
        self.show()
 
    def createTable(self):
       # Create table #
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.move(0,0)
 
        # table selection change #
        self.tableWidget.doubleClicked.connect(self.on_click)
 
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
 




# Choose The size of the puzzle #
class SizePuzz(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'N Puzzle - Size Choice'
        self.left = 1000
        self.top = 500
        self.width = 640
        self.height = 480
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Box for the integer #
        self.getInteger()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.show()
 
    def getInteger(self):
        global puzzleList
        global sizeChoice
        i, okPressed = QInputDialog.getInt(self, "Get integer","Define the size of a column:", 3, 3, 9, 1)
        if okPressed:
            sizeChoice = int(i)
            print(i)
            # MAKE that a tuple of tuple
            puzzleList = puzzleGenerator(sizeChoice)
            # print(puzzleList)
            self.close()
        else :
            print("Cancel :'(")
            self.close()
            sys.exit()


# Choose of the Heuristic #
class App(QDialog):
 
    def __init__(self):
        super().__init__()
        self.title = 'N Puzzle - Heuristic Choice'
        self.left = 1000
        self.top = 500
        self.width = 640
        self.height = 480
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Horizontal Layout to align buttons #
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

        # first button : Manhattan #
        manhattanButton = QPushButton('Manhattan Distance', self)
        manhattanButton.clicked.connect(self.on_click_manhattan)
        layout.addWidget(manhattanButton)

        # second button : Manhattan + Linear conflict #
        manLinConfButton = QPushButton('Manhattan + Linear Conflict', self)
        manLinConfButton.clicked.connect(self.on_click_manLinConfButton)
        layout.addWidget(manLinConfButton)

        # third Button: Not in place box #
        notInPlaceButton = QPushButton('Not in Place', self)
        notInPlaceButton.clicked.connect(self.on_click_notInPlace)
        layout.addWidget(notInPlaceButton)

        # fourth Button: n-MaxSwap ou Gashing #
        maxSwapButton = QPushButton('n-MaxSwap', self)
        maxSwapButton.clicked.connect(self.on_click_gusching)
        layout.addWidget(maxSwapButton)

        self.horizontalGroupBox.setLayout(layout)
 
    @pyqtSlot()

    def on_click_manhattan(self):
        global heuristicChoice
        print('Manhattan choosen')
        heuristicChoice = 'md'
        startFromGui(sizeChoice, puzzleList, heuristicChoice)
        self.accept()
    def on_click_manLinConfButton(self):
        global heuristicChoice
        print('Manhattan and Linear Conflict choosen')
        heuristicChoice = 'lc'
        startFromGui(sizeChoice, puzzleList, heuristicChoice)
        self.accept()
    def on_click_notInPlace(self):
        global heuristicChoice
        print('Not in place choosen')
        heuristicChoice = 'np'
        startFromGui(sizeChoice, puzzleList, heuristicChoice)
        self.accept()
    def on_click_gusching(self):
        global heuristicChoice
        print('n-MaxSwap ou Gushing choosen')
        heuristicChoice = 'gt'
        startFromGui(sizeChoice, puzzleList, heuristicChoice)
        self.accept()

def strat2emeWindowTest():
    sys.exit(app.exec_())
    # app = QApplication(sys.argv)
    ex2 = DisplayPath()
    # sys.exit(app.exec_())


def startFromGui(size, puzzleList, heuristicChoice):
    global retPath
    print("size : ", size , " puzzleList : ", puzzleList, " heuristic Choice : ", heuristicChoice)
#   ADD this part when parse.py is ready ##   
#   init(start)
#   retPath = doit(start)

    # ATTENTION remove next line (just for) ##
    retPath = [((1, 2, 3), (8, 0, 4), (7, 6, 5)), ((1, 2, 3), (0, 8, 4), (7, 6, 5)), ((0, 2, 3), (1, 8, 4), (7, 6, 5)), ((2, 0, 3), (1, 8, 4), (7, 6, 5)), ((2, 8, 3), (1, 0, 4), (7, 6, 5)), ((2, 8, 3), (1, 6, 4), (7, 0, 5)), ((2, 8, 3), (1, 6, 4), (0, 7, 5)), ((2, 8, 3), (0, 6, 4), (1, 7, 5)), ((2, 8, 3), (6, 0, 4), (1, 7, 5)), ((2, 8, 3), (6, 4, 0), (1, 7, 5)), ((2, 8, 3), (6, 4, 5), (1, 7, 0)), ((2, 8, 3), (6, 4, 5), (1, 0, 7)), ((2, 8, 3), (6, 4, 5), (0, 1, 7)),((2, 8, 3), (0, 4, 5), (6, 1, 7)), ((2, 8, 3), (4, 0, 5), (6, 1, 7)), ((2, 8, 3), (4, 5, 0), (6, 1, 7)), ((2, 8, 0), (4, 5, 3), (6, 1, 7)), ((2, 0, 8), (4, 5, 3), (6, 1, 7)), ((0, 2, 8), (4, 5, 3), (6, 1, 7)), ((4, 2, 8), (0, 5, 3), (6, 1, 7)), ((4, 2, 8), (5, 0, 3), (6, 1, 7)), ((4, 2, 8), (5, 3, 0), (6, 1, 7)), ((4, 2, 0), (5, 3, 8), (6, 1, 7)), ((4, 0, 2), (5, 3, 8), (6, 1, 7)), ((0, 4, 2), (5, 3, 8), (6, 1, 7)), ((5, 4, 2), (0, 3, 8), (6, 1, 7)), ((5, 4, 2), (3, 0, 8), (6, 1, 7)), ((5, 4, 2), (3, 1, 8), (6, 0, 7)), ((5, 4, 2), (3, 1, 8), (0, 6, 7))]
    print("path = ", retPath)
    strat2emeWindowTest()
    # ex2 = DisplayPath()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sizePuzz = SizePuzz()
    print("in the main: ", puzzleList)
    ex = App()
    print("len: ",len(retPath))
    # ex2 = DisplayPath()
    sys.exit(app.exec_())

