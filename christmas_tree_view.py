from PySide2.QtCore import Signal, Slot
from PySide2.QtGui import QBrush, QPen, QFont, QShowEvent
from PySide2.QtWidgets import QWidget, QMessageBox, QGraphicsScene, QGraphicsItem
from PySide2.QtCore import Qt
from graphics_view import Ui_Form


class ChristmasTreeView(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.scene = QGraphicsScene(self)
        self.ui.graphicsView.setScene(self.scene)

    def showEvent(self, event:QShowEvent):
        self.draw_stuff()

    def draw_stuff(self):
        greenBrush = QBrush(Qt.green)
        blueBrush = QBrush(Qt.blue)
        outlinePen = QPen(Qt.black)
        outlinePen.setWidth(2)
        scene_width = self.ui.graphicsView.viewport().width()
        mappedRect = self.ui.graphicsView.mapToScene(self.ui.graphicsView.viewport().geometry()).boundingRect()
        print(str(mappedRect.width()))
        rectangle = self.scene.addRect(0, 0, scene_width, 100, outlinePen, blueBrush)
        ellipse = self.scene.addEllipse(0, -100, 300, 60, outlinePen, greenBrush)
        text = self.scene.addText("something texty", QFont("Arial", 20))
        text.setFlag(QGraphicsItem.ItemIsMovable)
