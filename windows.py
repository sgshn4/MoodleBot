from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel
from PyQt5 import QtWidgets
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainLayout = QtWidgets.QGridLayout()
        self.table = QtWidgets.QTableView()
        self.calibrationButton = QtWidgets.QPushButton()
        self.calibrationButton.setText("Calibrate")
        self.addSubhectButton = QtWidgets.QPushButton()
        self.addSubhectButton.setText("Add Subject")
        self.runButton = QtWidgets.QPushButton()
        self.runButton.setText("Run!")
        self.mainLayout.addWidget(self.calibrationButton, 0, 1)
        self.mainLayout.addWidget(self.addSubhectButton, 1, 1)
        self.mainLayout.addWidget(self.runButton, 2, 1)
        self.mainLayout.addWidget(self.table, 0, 0)
        self.calibrationButton.clicked.connect(self.calibrationButtonClicked)
        self.addSubhectButton.clicked.connect(self.addButtonClicked)
        self.runButton.clicked.connect(self.runButtonClicked)
        self.widget = QWidget()
        self.widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("MoodleBot")

    def addButtonClicked(self):
        print('1')

    def runButtonClicked(self):
        print('2')

    def calibrationButtonClicked(self):
        print('3')
        self.w = CalibrationWidget()
        self.w.show()


class CalibrationWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QGridLayout()
        self.stageLabel = QLabel("Stage")
        self.coordinatesLabel = QLabel("X:n Y:n")
        self.changeButton = QPushButton()
        self.changeButton.setText("Change")
        self.changeButton.clicked.connect()
        self.nextButton = QPushButton()
        self.nextButton.setText("Next")
        self.nextButton.clicked.connect(self.nextButtonClicked)
        self.layout.addWidget(self.stageLabel, 0, 0)
        self.layout.addWidget(self.coordinatesLabel, 1, 0)
        self.layout.addWidget(self.changeButton, 2, 0)
        self.layout.addWidget(self.nextButton, 2, 1)
        self.setLayout(self.layout)

    def nextButtonClicked(self):
        pass

    def changeButtonClicked(self):
        pass


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()