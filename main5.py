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
        self.stack.addWidget(glWidget1())
        self.stack.addWidget(glWidget2())
        self.stack.addWidget(glWidget3())
        self.stack.addWidget(glWidget4())
        self.stack.addWidget(glWidget5())
        self.stack.addWidget(glWidget6())
        self.stack.addWidget(glWidget7())
        self.stack.addWidget(glWidget8())
        self.stack.addWidget(glWidget9())
        self.stack.addWidget(glWidget10())

        buttonsLayout = QtWidgets.QVBoxLayout()
        self.box = QComboBox()
        self.box.setMinimumSize(180, 20)
        self.box.addItems(["GL_POINTS", "GL_LINES", "GL_LINE_STRIP", "GL_LINE_LOOP", "GL_TRIANGLES", "GL_TRIANGLE_STRIP",
                   "GL_TRIANGLE_FAN", "GL_QUADS", "GL_QUAD_STRIP", "GL_POLYGON"])
        self.box.activated[int].connect(self.stack.setCurrentIndex)
        self.lbl = QLabel("Выбрано: GL_POINTS", self)
        self.box.activated[str].connect(self.activated_box)
        buttonsLayout.addWidget(self.box)
        buttonsLayout.addWidget(self.lbl)

        self.lbltests = QLabel("\nТест отсечения", self)
        self.boxscissor = QCheckBox("Активировать", self)
        self.boxscissor.stateChanged.connect(self.set_scissor)
        self.lblx = QLabel("X", self)
        self.sliderx = QSlider(Qt.Orientation.Horizontal, self)
        self.sliderx.setRange(0, 240)
        self.sliderx.valueChanged.connect(self.update_scissorsx)
        buttonsLayout.addWidget(self.lbltests)
        buttonsLayout.addWidget(self.boxscissor)
        buttonsLayout.addWidget(self.lblx)
        buttonsLayout.addWidget(self.sliderx)
        self.lbly = QLabel("Y", self)
        self.slidery = QSlider(Qt.Orientation.Horizontal, self)
        self.slidery.setRange(0, 240)
        self.slidery.valueChanged.connect(self.update_scissorsy)
        buttonsLayout.addWidget(self.lbly)
        buttonsLayout.addWidget(self.slidery)

        self.lbltesta = QLabel("\nТест прозрачности", self)
        self.boxalpha = QComboBox()
        self.boxalpha.setMinimumSize(180, 20)
        self.boxalpha.addItems(
            ["GL_NEVER", "GL_LESS", "GL_EQUAL", "GL_LEQUAL", "GL_GREATER", "GL_NOTEQUAL",
             "GL_GEQUAL", "GL_ALWAYS"])
        self.boxalpha.setCurrentIndex(7)
        self.boxalpha.activated[str].connect(self.activated_boxalpha)
        self.lblalpha = QLabel("Alpha: 0.0", self)
        self.slideralpha = QSlider(Qt.Orientation.Horizontal, self)
        self.slideralpha.setRange(0, 100)
        self.slideralpha.valueChanged.connect(self.update_alpha)
        buttonsLayout.addWidget(self.lbltesta)
        buttonsLayout.addWidget(self.boxalpha)
        buttonsLayout.addWidget(self.lblalpha)
        buttonsLayout.addWidget(self.slideralpha)

        self.lbltestb = QLabel("\nТест смешения цветов", self)
        self.lblsfactor = QLabel("sfactor", self)
        self.boxsfactor = QComboBox()
        self.boxsfactor.setMinimumSize(180, 20)
        self.boxsfactor.addItems(
            ["GL_ZERO", "GL_ONE", "GL_DST_COLOR", "GL_ONE_MINUS_DST_COLOR", "GL_SRC_ALPHA", "GL_ONE_MINUS_SRC_ALPHA",
             "GL_DST_ALPHA", "GL_ONE_MINUS_DST_ALPHA", "GL_SRC_ALPHA_SATURATE"])
        self.boxsfactor.setCurrentIndex(1)
        self.boxsfactor.activated[str].connect(self.activated_boxsfactor)
        self.lbldfactor = QLabel("dfactor", self)
        self.boxdfactor = QComboBox()
        self.boxdfactor.setMinimumSize(180, 20)
        self.boxdfactor.addItems(
            ["GL_ZERO", "GL_ONE", "GL_SRC_COLOR", "GL_ONE_MINUS_SRC_COLOR", "GL_SRC_ALPHA", "GL_ONE_MINUS_SRC_ALPHA",
             "GL_DST_ALPHA", "GL_ONE_MINUS_DST_ALPHA"])
        self.boxdfactor.activated[str].connect(self.activated_boxdfactor)
        buttonsLayout.addWidget(self.lbltestb)
        buttonsLayout.addWidget(self.lblsfactor)
        buttonsLayout.addWidget(self.boxsfactor)
        buttonsLayout.addWidget(self.lbldfactor)
        buttonsLayout.addWidget(self.boxdfactor)
        buttonsLayout.addStretch()

        mainLayout = QtWidgets.QHBoxLayout()
        widgetLayout = QtWidgets.QHBoxLayout()
        widgetLayout.addWidget(self.stack)
        mainLayout.addLayout(widgetLayout)
        mainLayout.addLayout(buttonsLayout)
        self.setLayout(mainLayout)
        self.setWindowTitle("Калмак Д.А. 0303")

    def activated_box(self, text):
        self.lbl.setText("Выбрано: " + text)

    def set_scissor(self, state):
        if state == Qt.Checked:
            for i in range(self.stack.__len__()):
                self.stack.widget(i).scissor_flag = True
                self.stack.widget(i).updateGL()
        else:
            for i in range(self.stack.__len__()):
                self.stack.widget(i).scissor_flag = False
                self.stack.widget(i).updateGL()

    def update_scissorsx(self, value):
        for i in range(self.stack.__len__()):
            self.stack.widget(i).x = value
            self.stack.widget(i).updateGL()

    def update_scissorsy(self, value):
        for i in range(self.stack.__len__()):
            self.stack.widget(i).y = value
            self.stack.widget(i).updateGL()

    def activated_boxalpha(self, text):
        for i in range(self.stack.__len__()):
            if text == "GL_NEVER":
                text = GL_NEVER
            if text == "GL_LESS":
                text = GL_LESS
            if text == "GL_EQUAL":
                text = GL_EQUAL
            if text == "GL_LEQUAL":
                text = GL_LEQUAL
            if text == "GL_GREATER":
                text = GL_GREATER
            if text == "GL_NOTEQUAL":
                text = GL_NOTEQUAL
            if text == "GL_GEQUAL":
                text = GL_GEQUAL
            if text == "GL_ALWAYS":
                text = GL_ALWAYS
            self.stack.widget(i).alphafunc = text
            self.stack.widget(i).updateGL()

    def update_alpha(self, value):
        self.lblalpha.setText("Alpha: " + str(value / 100))
        for i in range(self.stack.__len__()):
            self.stack.widget(i).alpharef = value
            self.stack.widget(i).updateGL()

    def activated_boxsfactor(self, text):
        for i in range(self.stack.__len__()):
            if text == "GL_ZERO":
                text = GL_ZERO
            if text == "GL_ONE":
                text = GL_ONE
            if text == "GL_DST_COLOR":
                text = GL_DST_COLOR
            if text == "GL_ONE_MINUS_DST_COLOR":
                text = GL_ONE_MINUS_DST_COLOR
            if text == "GL_SRC_ALPHA":
                text = GL_SRC_ALPHA
            if text == "GL_ONE_MINUS_SRC_ALPHA":
                text = GL_ONE_MINUS_SRC_ALPHA
            if text == "GL_DST_ALPHA":
                text = GL_DST_ALPHA
            if text == "GL_ONE_MINUS_DST_ALPHA":
                text = GL_ONE_MINUS_DST_ALPHA
            if text == "GL_SRC_ALPHA_SATURATE":
                text = GL_SRC_ALPHA_SATURATE
            self.stack.widget(i).sfact = text
            self.stack.widget(i).updateGL()

    def activated_boxdfactor(self, text):
        for i in range(self.stack.__len__()):
            if text == "GL_ZERO":
                text = GL_ZERO
            if text == "GL_ONE":
                text = GL_ONE
            if text == "GL_SRC_COLOR":
                text = GL_SRC_COLOR
            if text == "GL_ONE_MINUS_SRC_COLOR":
                text = GL_ONE_MINUS_SRC_COLOR
            if text == "GL_SRC_ALPHA":
                text = GL_SRC_ALPHA
            if text == "GL_ONE_MINUS_SRC_ALPHA":
                text = GL_ONE_MINUS_SRC_ALPHA
            if text == "GL_DST_ALPHA":
                text = GL_DST_ALPHA
            if text == "GL_ONE_MINUS_DST_ALPHA":
                text = GL_ONE_MINUS_DST_ALPHA
            self.stack.widget(i).dfact = text
            self.stack.widget(i).updateGL()


class glWidget0(QGLWidget):
    def __init__(self, parent=None):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(480, 480)
        self.w = 480
        self.h = 480
        self.scissor_flag = False
        self.x = 0
        self.y = 0
        self.alphafunc = GL_ALWAYS
        self.alpharef = 0
        self.sfact = GL_ONE
        self.dfact = GL_ZERO

    def initializeGL(self):
        glClearColor(0, 0, 0, 0.1)
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


class glWidget1(glWidget0):
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(-2.5, 0.5, -5.0)
        glColor4f(0.5, 1.0, 0.5, 0.5)
        glDepthMask(GL_FALSE)
        glEnable(GL_BLEND)
        glBlendFunc(self.sfact, self.dfact)
        glEnable(GL_ALPHA_TEST)
        glAlphaFunc(self.alphafunc, self.alpharef / 100)
        if self.scissor_flag:
            glEnable(GL_SCISSOR_TEST)
            glScissor(self.x, self.y, int(self.w / 2), int(self.h / 2))
        glBegin(GL_POINTS)
        glVertex3f(2.0, -1.2, 0.0)
        glVertex3f(2.6, 0.0, 0.0)
        glVertex3f(2.9, -1.2, 0.0)
        glEnd()
        glDisable(GL_SCISSOR_TEST)
        glDisable(GL_ALPHA_TEST)
        glDepthMask(GL_TRUE)
        glDisable(GL_BLEND)
        glFlush()


class glWidget2(glWidget0):
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(-2.5, 0.5, -5.0)
        glColor4f(0.5, 1.0, 0.5, 0.5)
        glDepthMask(GL_FALSE)
        glEnable(GL_BLEND)
        glBlendFunc(self.sfact, self.dfact)
        glEnable(GL_ALPHA_TEST)
        glAlphaFunc(self.alphafunc, self.alpharef / 100)
        if self.scissor_flag:
            glEnable(GL_SCISSOR_TEST)
            glScissor(self.x, self.y, int(self.w / 2), int(self.h / 2))
        glBegin(GL_LINES)
        glVertex3f(2.0, -1.2, 0.0)
        glVertex3f(2.6, 0.0, 0.0)
        glVertex3f(2.9, -1.2, 0.0)
        glVertex3f(2.9, 1.2, 0.0)
        glEnd()
        glDisable(GL_SCISSOR_TEST)
        glDisable(GL_ALPHA_TEST)
        glDepthMask(GL_TRUE)
        glDisable(GL_BLEND)
        glFlush()


class glWidget3(glWidget0):
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(-2.5, 0.5, -5.0)
        glColor4f(0.5, 1.0, 0.5, 0.5)
        glEnable(GL_LINE_STIPPLE)
        glLineStipple(1, 0x0101)
        glDepthMask(GL_FALSE)
        glEnable(GL_BLEND)
        glBlendFunc(self.sfact, self.dfact)
        glEnable(GL_ALPHA_TEST)
        glAlphaFunc(self.alphafunc, self.alpharef / 100)
        if self.scissor_flag:
            glEnable(GL_SCISSOR_TEST)
            glScissor(self.x, self.y, int(self.w / 2), int(self.h / 2))
        glBegin(GL_LINE_STRIP)
        glVertex3f(2.0, -1.2, 0.0)
        glVertex3f(2.6, 0.0, 0.0)
        glVertex3f(2.9, -1.2, 0.0)
        glVertex3f(2.9, 1.2, 0.0)
        glEnd()
        glDisable(GL_SCISSOR_TEST)
        glDisable(GL_ALPHA_TEST)
        glDepthMask(GL_TRUE)
        glDisable(GL_BLEND)
        glFlush()


class glWidget4(glWidget0):
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(-2.5, 0.5, -5.0)
        glColor4f(0.5, 1.0, 0.5, 0.5)
        glEnable(GL_LINE_STIPPLE)
        glLineStipple(1, 0x00FF)
        glDepthMask(GL_FALSE)
        glEnable(GL_BLEND)
        glBlendFunc(self.sfact, self.dfact)
        glEnable(GL_ALPHA_TEST)
        glAlphaFunc(self.alphafunc, self.alpharef / 100)
        if self.scissor_flag:
            glEnable(GL_SCISSOR_TEST)
            glScissor(self.x, self.y, int(self.w / 2), int(self.h / 2))
        glBegin(GL_LINE_LOOP)
        glVertex3f(2.0, -1.2, 0.0)
        glVertex3f(2.6, 0.0, 0.0)
        glVertex3f(2.9, -1.2, 0.0)
        glVertex3f(2.9, 1.2, 0.0)
        glEnd()
        glDisable(GL_SCISSOR_TEST)
        glDisable(GL_ALPHA_TEST)
        glDepthMask(GL_TRUE)
        glDisable(GL_BLEND)
        glFlush()


class glWidget5(glWidget0):
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(-2.5, 0.5, -5.0)
        glColor4f(0, 1.0, 0, 0.5)
        glPolygonMode(GL_FRONT, GL_FILL)
        glDepthMask(GL_FALSE)
        glEnable(GL_BLEND)
        glBlendFunc(self.sfact, self.dfact)
        glEnable(GL_ALPHA_TEST)
        glAlphaFunc(self.alphafunc, self.alpharef / 100)
        if self.scissor_flag:
            glEnable(GL_SCISSOR_TEST)
            glScissor(self.x, self.y, int(self.w / 2), int(self.h / 2))
        glBegin(GL_TRIANGLES)
        glVertex3f(1.0, -1.2, 0.0)
        glVertex3f(1.6, 0.0, 0.0)
        glVertex3f(2.9, -1.2, 0.0)
        glEnd()
        glColor4f(1.0, 0, 0, 0.4)
        glBegin(GL_TRIANGLES)
        glVertex3f(2.0, -1.2, 0.0)
        glVertex3f(2.6, 0.0, 0.0)
        glVertex3f(2.9, -1.2, 0.0)
        glEnd()
        glDisable(GL_SCISSOR_TEST)
        glDisable(GL_ALPHA_TEST)
        glDepthMask(GL_TRUE)
        glDisable(GL_BLEND)
        glFlush()


class glWidget6(glWidget0):
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(-2.5, 0.5, -5.0)
        glColor4f(0.5, 1.0, 0.5, 0.5)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glDepthMask(GL_FALSE)
        glEnable(GL_BLEND)
        glBlendFunc(self.sfact, self.dfact)
        glEnable(GL_ALPHA_TEST)
        glAlphaFunc(self.alphafunc, self.alpharef / 100)
        if self.scissor_flag:
            glEnable(GL_SCISSOR_TEST)
            glScissor(self.x, self.y, int(self.w / 2), int(self.h / 2))
        glBegin(GL_TRIANGLE_STRIP)
        glVertex3f(2.0, -1.2, 0.0)
        glVertex3f(2.6, 0.0, 0.0)
        glVertex3f(2.9, -1.2, 0.0)
        glVertex3f(3.9, 0.2, 0.0)
        glVertex3f(3.9, -1.2, 0.0)
        glEnd()
        glDisable(GL_SCISSOR_TEST)
        glDisable(GL_ALPHA_TEST)
        glDepthMask(GL_TRUE)
        glDisable(GL_BLEND)
        glFlush()


class glWidget7(glWidget0):
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(-2.5, 0.5, -5.0)
        glColor4f(0.5, 1.0, 0.5, 0.5)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glDepthMask(GL_FALSE)
        glEnable(GL_BLEND)
        glBlendFunc(self.sfact, self.dfact)
        glEnable(GL_ALPHA_TEST)
        glAlphaFunc(self.alphafunc, self.alpharef / 100)
        if self.scissor_flag:
            glEnable(GL_SCISSOR_TEST)
            glScissor(self.x, self.y, int(self.w / 2), int(self.h / 2))
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(2.0, -1.2, 0.0)
        glVertex3f(2.6, 0.0, 0.0)
        glVertex3f(2.9, -1.2, 0.0)
        glVertex3f(2.0, -2.2, 0.0)
        glVertex3f(0.9, -1.2, 0.0)
        glEnd()
        glDisable(GL_SCISSOR_TEST)
        glDisable(GL_ALPHA_TEST)
        glDepthMask(GL_TRUE)
        glDisable(GL_BLEND)
        glFlush()


class glWidget8(glWidget0):
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(-2.5, 0.5, -5.0)
        glColor4f(0.5, 1.0, 0.5, 0.5)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glDepthMask(GL_FALSE)
        glEnable(GL_BLEND)
        glBlendFunc(self.sfact, self.dfact)
        glEnable(GL_ALPHA_TEST)
        glAlphaFunc(self.alphafunc, self.alpharef / 100)
        if self.scissor_flag:
            glEnable(GL_SCISSOR_TEST)
            glScissor(self.x, self.y, int(self.w / 2), int(self.h / 2))
        glBegin(GL_QUADS)
        glVertex3f(2.0, -1.2, 0.0)
        glVertex3f(3.0, -1.2, 0.0)
        glVertex3f(3.0, 0.2, 0.0)
        glVertex3f(2.0, 0.2, 0.0)
        glEnd()
        glDisable(GL_SCISSOR_TEST)
        glDisable(GL_ALPHA_TEST)
        glDepthMask(GL_TRUE)
        glDisable(GL_BLEND)
        glFlush()


class glWidget9(glWidget0):
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(-2.5, 0.5, -5.0)
        glColor4f(0.5, 1.0, 0.5, 0.5)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glDepthMask(GL_FALSE)
        glEnable(GL_BLEND)
        glBlendFunc(self.sfact, self.dfact)
        glEnable(GL_ALPHA_TEST)
        glAlphaFunc(self.alphafunc, self.alpharef / 100)
        if self.scissor_flag:
            glEnable(GL_SCISSOR_TEST)
            glScissor(self.x, self.y, int(self.w / 2), int(self.h / 2))
        glBegin(GL_QUAD_STRIP)
        glVertex3f(2.0, -1.2, 0.0)
        glVertex3f(2.0, 0.2, 0.0)
        glVertex3f(3.0, -1.2, 0.0)
        glVertex3f(3.0, 0.2, 0.0)
        glVertex3f(4.0, -1.2, 0.0)
        glVertex3f(4.0, 0.2, 0.0)
        glEnd()
        glDisable(GL_SCISSOR_TEST)
        glDisable(GL_ALPHA_TEST)
        glDepthMask(GL_TRUE)
        glDisable(GL_BLEND)
        glFlush()


class glWidget10(glWidget0):
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(-2.5, 0.5, -5.0)
        glColor4f(0.5, 1.0, 0.5, 0.5)
        glPolygonMode(GL_FRONT, GL_FILL)
        glDepthMask(GL_FALSE)
        glEnable(GL_BLEND)
        glBlendFunc(self.sfact, self.dfact)
        glEnable(GL_ALPHA_TEST)
        glAlphaFunc(self.alphafunc, self.alpharef / 100)
        if self.scissor_flag:
            glEnable(GL_SCISSOR_TEST)
            glScissor(self.x, self.y, int(self.w / 2), int(self.h / 2))
        glBegin(GL_POLYGON)
        glVertex2f(2.0, -0.2)
        glVertex2f(2.5, 0.7)
        glVertex2f(3.0, 1.2)
        glVertex2f(4.0, 0.2)
        glVertex2f(2.8, -0.5)
        glEnd()
        glDisable(GL_SCISSOR_TEST)
        glDisable(GL_ALPHA_TEST)
        glDepthMask(GL_TRUE)
        glDisable(GL_BLEND)
        glFlush()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qWindow = QtWidgets.QMainWindow()
    window = mainWindow(qWindow)
    window.show()
    sys.exit(app.exec_())