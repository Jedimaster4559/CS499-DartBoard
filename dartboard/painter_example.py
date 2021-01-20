import math
import sys

from PySide2.QtCore import Qt, QPoint
from PySide2.QtGui import QPen, QBrush, QPolygon
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QApplication

from backend.models import DartboardHit


class Window(QGraphicsView):

    # constructor for QGraphicsView subclass
    def __init__(self, parent=None):

        # call parent constructor
        super().__init__(parent)

        # set and set scene for QGraphicsView
        self.scene = QGraphicsScene(self)
        self.scene.setBackgroundBrush(QBrush(Qt.yellow))
        self.setScene(self.scene)

        # set variables and constants
        self.WindowSizeX = 300
        self.WindowSizeY = 300
        self.WindowPosX = 300
        self.WindowPosY = 300
        self.regionConstant = 20
        self.radius = 0

        # this list holds the points
        self.points = []

        # names window
        self.setWindowTitle("Pyside2 Drawing Polygon")

        # sets initial geometry for the window
        self.setGeometry(self.WindowPosX, self.WindowPosY, self.WindowSizeX, self.WindowSizeY)

        # draws the circles and dots for the first time
        self.DrawRegions()

        # shows the window
        self.show()

    # this function is called when a point is placed on the window
    def mousePressEvent(self, event):

        # this call could be used to get your mock points
        print(event.pos())

        #
        hit = DartboardHit(x=event.pos().x(), y=event.pos().y())
        hit.save()
        print(DartboardHit.objects.all())

        # this stores the real position of the click by adding together the top left position of the window with the click position relative to the window
        realPosition = QPoint(event.pos().x() + self.WindowPosX, event.pos().y() + self.WindowPosY)

        # check for collisions with each region
        if (self.bullseye.containsPoint(realPosition, Qt.OddEvenFill)):
            print("bullseye")
        elif (self.outer_bullseye.containsPoint(realPosition, Qt.OddEvenFill)):
            print("outer bullseye")

        # this line adds an entry for the point that was just placed. It calculates the x and y distance from the center of the circle divided by the current radius of the circle
        # this is used to relocate the points later when the window is resized
        self.points.append([(event.pos().x() - (self.WindowSizeX / 2.0)) / self.radius,
                            (event.pos().y() - (self.WindowSizeY / 2.0)) / self.radius])

        # this line draws the point on the screen where the mouse was clicked
        self.scene.addEllipse(self.WindowPosX + event.pos().x(), self.WindowPosY + event.pos().y(), 3, 3, QPen(),
                              QBrush(Qt.white))

    # this function is called when the window is resized
    def resizeEvent(self, event):
        # print(self.sceneRect())

        # these lines set the variables initialized in the constructor to their new values
        self.WindowSizeX = event.size().width()
        self.WindowSizeY = event.size().height()
        self.WindowPosX = self.pos().x()
        self.WindowPosY = self.pos().y()

        # this line sets the Scene's geometry based on the newly resized window
        self.scene.setSceneRect(self.WindowPosX, self.WindowPosY, self.WindowSizeX, self.WindowSizeY)

        # recall the drawing function to replace the circles and points with the new size
        self.DrawRegions()

        # tbh idek what this does
        super().resizeEvent(event)

    # helper used to calculate circular coordinates
    def GetPointsInCircle(self, r, n=100):
        pi = math.pi
        return [(math.cos(2 * pi / n * x) * r, math.sin(2 * pi / n * x) * r) for x in range(0, n + 1)]

    # function used to draw all the shapes
    def DrawRegions(self):

        # clear the scene
        self.scene.clear()

        # create polygon and add points to it
        self.outer_bullseye = QPolygon()
        self.radius = (self.WindowSizeX + self.WindowSizeY) / self.regionConstant * 2
        outer_bullseye_points = self.GetPointsInCircle(self.radius)

        for i in outer_bullseye_points:
            self.outer_bullseye.push_back(QPoint(i[0] + self.WindowPosX + (self.WindowSizeX / 2.0),
                                                 i[1] + self.WindowPosY + (self.WindowSizeY / 2.0)))

        # create polygon and add points to it
        self.bullseye = QPolygon()
        bullseye_points = self.GetPointsInCircle((self.WindowSizeX + self.WindowSizeY) / self.regionConstant)

        for i in bullseye_points:
            self.bullseye.push_back(QPoint(i[0] + self.WindowPosX + (self.WindowSizeX / 2.0),
                                           i[1] + self.WindowPosY + (self.WindowSizeY / 2.0)))

        # draw the the bullseyes
        self.scene.addPolygon(self.outer_bullseye, QPen(), QBrush(Qt.green))
        self.scene.addPolygon(self.bullseye, QPen(), QBrush(Qt.red))

        # calculate and draw the points that were initially placed before resize
        for p in self.points:
            x_dec = self.radius * p[0]
            y_dec = self.radius * p[1]
            self.scene.addEllipse(self.WindowPosX + (self.WindowSizeX / 2.0) + x_dec,
                                  self.WindowPosY + (self.WindowSizeY / 2.0) + y_dec, 3, 3, QPen(), QBrush(Qt.white))


# runner code

# create application and window
def open():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
