from asyncore import write, read
from mailcap import show
from tkinter import filedialog, END, BOTH, Text, Menu

from PyQt5 import QtWidgets, QtGui, QtCore

font_but = QtGui.QFont()
font_but.setFamily("Segoe UI Symbol")
font_but.setPointSize(10)
font_but.setWeight(95)


class PushBut1(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(PushBut1, self).__init__(parent)
        self.setMouseTracking(True)
        self.setStyleSheet(
            "margin: 1px; padding: 7px; background-color: rgba(1,255,255,100); color: rgba(0,190,255,255); border-style: solid;"
            "border-radius: 3px; border-width: 0.5px; border-color: rgba(127,127,255,255);")

    def enterEvent(self, event):
        if self.isEnabled() is True:
            self.setStyleSheet(
                "margin: 1px; padding: 7px; background-color: rgba(1,255,255,100); color: rgba(0,230,255,255);"
                "border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: rgba(0,230,255,255);")
        if self.isEnabled() is False:
            self.setStyleSheet(
                "margin: 1px; padding: 7px; background-color: rgba(1,255,255,100); color: rgba(0,190,255,255); border-style: solid;"
                "border-radius: 3px; border-width: 0.5px; border-color: rgba(127,127,255,255);")

    def leaveEvent(self, event):
        self.setStyleSheet(
            "margin: 1px; padding: 7px; background-color: rgba(1,255,255,100); color: rgba(0,190,255,255); border-style: solid;"
            "border-radius: 3px; border-width: 0.5px; border-color: rgba(127,127,255,255);")


class PyQtApp(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("TextEditor Application")
        self.setWindowIcon(QtGui.QIcon("Path/to/Your/image/file.png"))
        self.setMinimumWidth(resolution.width() / 3)
        self.setMinimumHeight(resolution.height() / 1.5)
        self.setStyleSheet(
            "QWidget {background-color: rgba(0,41,59,255);} QScrollBar:horizontal {width: 1px; height: 1px;"
            "background-color: rgba(0,41,59,255);} QScrollBar:vertical {width: 1px; height: 1px;"
            "background-color: rgba(0,41,59,255);}")
        self.textf = QtWidgets.QTextEdit(self)
        self.textf.setPlaceholderText("Type Something...")
        self.textf.setStyleSheet(
            "margin: 1px; padding: 7px; background-color: rgba(0,255,255,100); color: rgba(0,190,255,255);"
            "border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: rgba(0,140,255,255);")
        self.but1 = PushBut1(self)
        self.but1.setText("Open")
        self.but1.setFixedWidth(72)
        self.but1.setFont(font_but)
        self.but2 = PushBut1(self)
        self.but2.setText("Save as")
        self.but2.setFixedWidth(72)
        self.but2.setFont(font_but)
        self.but3 = PushBut1(self)
        self.but3.setText("Save")
        self.but3.setFixedWidth(72)
        self.but3.setFont(font_but)
        self.but4 = PushBut1(self)
        self.but4.setText("Edit")
        self.but4.setFixedWidth(72)
        self.but4.setFont(font_but)
        self.but5 = PushBut1(self)
        self.but5.setText("")
        self.but5.setFixedWidth(72)
        self.but5.setFont(font_but)
        self.but6 = PushBut1(self)
        self.but6.setText("")
        self.but6.setFixedWidth(72)
        self.but6.setFont(font_but)
        self.but7 = PushBut1(self)
        self.but7.setText("")
        self.but7.setFixedWidth(72)
        self.but7.setFont(font_but)
        self.lb1 = QtWidgets.QLabel(self)
        self.lb1.setFixedWidth(72)
        self.lb1.setFixedHeight(72)
        self.grid1 = QtWidgets.QGridLayout()
        self.grid1.addWidget(self.textf, 0, 0, 14, 13)
        self.grid1.addWidget(self.but1, 0, 14, 1, 1)
        self.grid1.addWidget(self.but2, 1, 14, 1, 1)
        self.grid1.addWidget(self.but3, 2, 14, 1, 1)
        self.grid1.addWidget(self.but4, 3, 14, 1, 1)
        self.grid1.addWidget(self.but5, 4, 14, 1, 1)
        self.grid1.addWidget(self.but6, 5, 14, 1, 1)
        self.grid1.addWidget(self.but7, 6, 14, 1, 1)
        self.grid1.addWidget(self.lb1, 12, 14, 1, 1)
        self.grid1.setContentsMargins(7, 7, 7, 7)
        self.setLayout(self.grid1)
        self.but1.clicked.connect(self.on_but1)
        self.but2.clicked.connect(self.on_but2)

    current_open_file = "no_file"
    def on_but1(self):
        self.textf.setStyleSheet(
            "margin: 1px; padding: 7px; background-color: rgba(1,255,217,100); color: rgba(0,190,255,255);"
            "border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: rgba(0,140,255,255);")

        open_return = filedialog.askopenfile(initialdir="", title="select file to open", filetypes=(("")))
        if (open_return != None):
            self.text_area.delete(1.0, END)
            for line in open_return:
                self.text_area.insert(open(), line, write, read, show)
            self.current_open_file = open_return.name
            self.current_open_file = open(read())
            open_return.close()


    def on_but2(self):
        txt = self.textf.toPlainText()
        try:
            img = QtGui.QPixmap(txt)
            self.lb1.setPixmap(img.scaledToWidth(72, QtCore.Qt.SmoothTransformation))

            f = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
            if f is None:
                return
                text2save = self.text_area.get(1.0, END)
                self.current_open_file = f.name
                f.write(text2save)
                f.close()
        except:
            pass

    def on_but3(self):
        txt = self.textf.toPlainText()
        try:
            img = QtGui.QPixmap(txt)
            self.lb1.setPixmap(img.scaledToWidth(72, QtCore.Qt.SmoothTransformation))

            if self.current_open_file == "no_file":
                self.save_as_file()
            else:
                f = open(self.current_open_file, "w+")
                f.write(self.text_area.get(1.0, END))
                f.close()
        except:
            pass


    # current_open_file = "no_file"
    # def open_file(self):
    #     open_return = filedialog.askopenfile(initialdir="/", title="select file to open", filetupes=(("text")))
    #     if (open_return != None):
    #         self.text_area.delete(1.0, END)
    #         for line in open_return:
    #             self.text_area.insert(END, line)
    #         self.current_open_file = open_return.name
    #         open_return.close()

    # def save_as_file(self):
    #     f = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    #     if f is None:
    #         return
    #         text2save = self.text_area.get(1.0, END)
    #         self.current_open_file = f.name
    #         f.write(text2save)
    #         f.close()

    # def save_file(self):
    #      if self.current_open_file == "no_file":
    #          self.save_as_file()
    #      else:
    #         f = open(self.current_open_file, "w+")
    #         f.write(self.text_area.get(1.0, END))
    #         f.close()

    def __init_subclass__(self, master):
        self.master = master
        self.text_area = Text()
        self.text_area.pack(fill=BOTH, expand=1)
        self.main_menu = Menu()
        self.master.config(menu=self.main_menu)

        self.file_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label="file", menu=self.file_menu)
        self.file_menu.add_command(label="Open", menu=self.open_file)
        self.file_menu.add_command(label="Save as", menu=self.save_as_file)
        self.file_menu.add_command(label="Save", menu=self.save_file)

        self.edit_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    desktop = QtWidgets.QApplication.desktop()
    resolution = desktop.availableGeometry()
    myapp = PyQtApp()
    myapp.setWindowOpacity(0.95)
    myapp.show()
    myapp.move(resolution.center() - myapp.rect().center())
    sys.exit(app.exec_())
else:
    desktop = QtWidgets.QApplication.desktop()
    resolution = desktop.availableGeometry()


