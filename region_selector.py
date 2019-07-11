import sys
import cv2
from screen_resolution import get_screen_res
from PyQt5 import QtWidgets, QtCore, QtGui
from screen_grab import grab_screen


class RegionSelector(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        width, height, left, top = get_screen_res()

        self.setGeometry(left, top, width, height)
        self.setWindowTitle('region_selctor')
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.4)
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.CrossCursor)
        )
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |
                            QtCore.Qt.WindowStaysOnTopHint)

        self.region = []

    def paintEvent(self, event):
        qt_painter = QtGui.QPainter(self)
        qt_painter.setPen(QtGui.QPen(QtGui.QColor('red'), 1))
        qt_painter.setBrush(QtGui.QColor(0, 0, 0, 255))
        qt_painter.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.close()

        # Selected windows x1,y1 top left. x2,y2 bottom right
        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())

        width = abs(x1-x2)
        height = abs(y1-y2)
        left = x1 - 1920
        top = y1

        self.region = [
            width,
            height,
            left,
            top,
        ]

    def get_region(self):
        return self.region


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = RegionSelector()
    window.show()
    # app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())
