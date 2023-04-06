import math
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5.QtCore import Qt
from PyQt5.QtOpenGL import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QComboBox, QStackedWidget, QSlider, QCheckBox)


class mainWindow(QWidget):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__()
        self.stack = QStackedWidget()
        self.stack.addWidget(glWidgetFractal())

        buttonsLayout = QtWidgets.QVBoxLayout()
        self.lblrecursiondepth = QLabel("Глубина рекурсии", self)
        self.sliderrecdepth = QSlider(Qt.Orientation.Horizontal, self)
        self.sliderrecdepth.setMinimum(1)
        self.sliderrecdepth.setMaximum(4)
        self.sliderrecdepth.valueChanged.connect(self.update_recdepth)
        buttonsLayout.addWidget(self.lblrecursiondepth)
        buttonsLayout.addWidget(self.sliderrecdepth)
        buttonsLayout.addStretch()

        mainLayout = QtWidgets.QHBoxLayout()
        widgetLayout = QtWidgets.QHBoxLayout()
        widgetLayout.addWidget(self.stack)
        mainLayout.addLayout(widgetLayout)
        mainLayout.addLayout(buttonsLayout)
        self.setLayout(mainLayout)
        self.setWindowTitle("Калмак Д.А. 0303")

    def update_recdepth(self, value):
        for i in range(self.stack.__len__()):
            self.stack.widget(i).level = value
            self.stack.widget(i).updateGL()


class glWidget0(QGLWidget):
    def __init__(self, parent=None):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(750, 720)
        self.w = 480
        self.h = 480
        self.level = 1
        self.count = 0

    def initializeGL(self):
        glClearColor(1.0, 1.0, 1.0, 0.1)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, 1, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        pass

    def resizeGL(self, w, h):
        self.w = w
        self.h = h
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspect = w / h
        gluPerspective(45.0, aspect, 0.1, 100)
        glMatrixMode(GL_MODELVIEW)


class glWidgetFractal(glWidget0):
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0, 0, -4.0)
        self.draw_spiral(0, 1, 1, [])
        self.count = 0

    def draw_spiral(self, level, scalex, scaley, xascop):
        if level == self.level:
            self.count += 1
            print(self.count)
            return
        a = 0.01
        b = 0.15
        k = 0
        h = 0.05
        r = 0.001
        count = 0
        countx = 0
        county = 0
        xy1 = []
        while k < 4.5 * math.pi:
            x = a * pow(2.718281, b * k) * math.cos(k)
            y = a * pow(2.718281, b * k) * math.sin(k)
            xy1.append([x + countx, y + county])
            glTranslatef(x, y, 0.0)
            countx += x
            county += y
            glColor4f(0.0, 0.0, 0.0, 0.5)
            quadObj = gluNewQuadric()
            if count % 6 == 0:
                gluSphere(quadObj, r, 50, 50)
            k += h
            r += 0.0002
            count += 1
            glFlush()
        glTranslatef(-countx, -county, 0)
        a2 = 0.006
        b2 = 0.15
        k = 0
        h = 0.05
        r = 0.001
        count = 0
        countx = 0
        county = 0
        xy2 = []
        while k < 4.5 * math.pi:
            x = a2 * pow(2.718281, b2 * k) * math.cos(k)
            y = a2 * pow(2.718281, b2 * k) * math.sin(k)
            xy2.append([x + countx, y + county])
            glTranslatef(x, y, 0.0)
            countx += x
            county += y
            glColor4f(0.85098, 0.38823, 0.81568, 0.5)
            quadObj = gluNewQuadric()
            if count % 4 == 0:
                gluSphere(quadObj, r, 50, 50)
            k += h
            r += 0.0002
            count += 1
            glFlush()
        glLoadIdentity()
        glTranslatef(0, 0, 0)
        xas = [[(xy1[i][0] + xy2[i][0]) / 2, (xy1[i][1] + xy2[i][1]) / 2] for i in range(len(xy1) - 1, -1, -1)]
        if level > 0:
            xas = xascop
        count_rotate = 0
        x_scale = scalex * 0.2
        y_scale = scaley * 0.2
        check = 1
        check_x = 0
        for i in range(0, len(xas), 5):
            glTranslatef(xas[i][0], xas[i][1], -4)
            glRotate(-60+count_rotate, xas[i][0], xas[i][1], -4)
            xascopy = [0 for j in range(0, len(xas))]
            for k in range(0, len(xas)):
                x_new = xas[i][0] + xas[k][0] * x_scale
                y_new = xas[i][1] + xas[k][1] * y_scale
                xascopy[k] = [(x_new - xas[i][0]) * math.cos((60-count_rotate) * math.pi / 180) - (y_new - xas[i][1]) * math.sin((60-count_rotate) * math.pi / 180) + xas[i][0],
                              (x_new - xas[i][0]) * math.sin((60-count_rotate) * math.pi / 180) + (y_new - xas[i][1]) * math.cos((60-count_rotate) * math.pi / 180) + xas[i][1]]
            glScale(x_scale, y_scale, 0)
            self.draw_spiral(level + 1, x_scale, y_scale, xascopy)
            glLoadIdentity()
            count_rotate += 5

            if check == 1:
                x_scale -= 0.005 * scalex
                y_scale -= 0.005 * scaley
            if check == 0:
                x_scale += 0.005 * scalex
                y_scale += 0.005 * scaley
            elif check == -1:
                x_scale -= 0.007 * scalex
                y_scale -= 0.007 * scaley
            if x_scale < 0.025 * scalex and check_x == 0:
                check = 0
                check_x = 1
            if x_scale > 0.07 * scalex and check_x == 1:
                check = -1
                check_x = 2


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qWindow = QtWidgets.QMainWindow()
    window = mainWindow(qWindow)
    window.show()
    sys.exit(app.exec_())