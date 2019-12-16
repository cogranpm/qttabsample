from PySide2.QtCore import Signal, Slot
from PySide2.QtGui import QBrush, QPen, QFont, QShowEvent, QResizeEvent
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

    def showEvent(self, event: QShowEvent):
        self.draw_stuff()

    def resizeEvent(self, event: QResizeEvent):
        self.draw_stuff()

    def draw_stuff(self):
        self.scene.clear()
        greenBrush = QBrush(Qt.green)
        blueBrush = QBrush(Qt.blue)
        outlinePen = QPen(Qt.black)
        outlinePen.setWidth(2)
        scene_width = self.ui.graphicsView.viewport().width()
        scene_height = self.ui.graphicsView.viewport().height()
        # for instruction, does it need to use the co-ordinate system of view
        mappedRect = self.ui.graphicsView.mapToScene(self.ui.graphicsView.viewport().geometry()).boundingRect()

        mid_pointw = scene_width / 2
        mid_pointy = scene_height / 2
        trunk_width = 20
        trunk = self.scene.addRect(mid_pointw - (trunk_width / 2), 0, trunk_width, scene_height, outlinePen, greenBrush)
        self.draw_branch(scene_width, mid_pointy, outlinePen, blueBrush)

        #map(lambda n: self.draw_branch(scene_width, 60 * n, outlinePen, blueBrush), iterations)
        currentY = mid_pointy
        currentYn = mid_pointy
        for n in range(10):
            self.draw_branch(scene_width, currentY, outlinePen, blueBrush)
            self.draw_branch(scene_width, currentYn, outlinePen, greenBrush)
            currentY = currentY + 30
            currentYn = currentYn - 30

            #self.draw_branch(scene_width, mid_pointy - 60, outlinePen, blueBrush)
        #self.draw_branch(scene_width, mid_pointy + 60, outlinePen, blueBrush)
        #ellipse = self.scene.addEllipse(0, -100, 300, 60, outlinePen, greenBrush)
        text = self.scene.addText("Python Tutorial", QFont("Arial", 20))
        text.setFlag(QGraphicsItem.ItemIsMovable)

    def draw_branch(self, scene_width, y, pen, brush):
        print(str(y))
        mid_pointw = scene_width / 2
        trunk_width = 20
        branch_height = 10
        trunk_left_edge = mid_pointw - (trunk_width / 2)
        trunk_right_edge = mid_pointw + (trunk_width / 2)
        right_branch = self.scene.addRect(trunk_right_edge, y, mid_pointw, branch_height, pen, brush)
        left_branch = self.scene.addRect(0, y, trunk_left_edge, branch_height, pen, brush)

