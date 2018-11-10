
from PyQt5.QtCore import (QLineF, QPointF, QRectF, Qt)
from PyQt5.QtGui import (QBrush, QColor, QPainter)
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem,
                             QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton)




# class do(QGraphicsItem):
#     def __init__(self):
#         super().__init__()
#         self.keaton = [1,1,1]
#     def paint(self):
#         painter.setPen(Qt.black)
#         painter.drawLine(0,100,300,100)
#         painter.drawLine(0,200,300,200)
#         painter.drawLine(100,0,100,300)
#         painter.drawLine(200,0,200,300)
#     def boundingRect(self):
#         return QRectF(0,0,300,300)
    


class Window(QGraphicsView):
    def __init__(self):
        super(Window, self).__init__()
        scene = QGraphicsScene(self)
        scene.setSceneRect(0, 0, 1000, 300)
        self.setScene(scene)
        self.setCacheMode(QGraphicsView.CacheBackground)
        # self.setWindowTitle("Tic Tac Toe")



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
    



