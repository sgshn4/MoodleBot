from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel
from PyQt5 import QtWidgets, QtCore
import sys
import calibration
import structures

lectures = []
browsername = ""
coordinates = []
runnable = False


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainLayout = QtWidgets.QGridLayout()
        self.table = QtWidgets.QTableView()
        self.calibrationButton = QtWidgets.QPushButton()
        self.calibrationButton.setText("Calibrate")
        self.addSubhectButton = QtWidgets.QPushButton()
        self.addSubhectButton.setText("Add Subject")
        self.changeBrowser = QtWidgets.QPushButton()
        self.changeBrowser.setText("Change Browser")
        self.runButton = QtWidgets.QPushButton()
        self.runButton.setText("Run!")
        self.mainLayout.addWidget(self.calibrationButton, 0, 1)
        self.mainLayout.addWidget(self.addSubhectButton, 1, 1)
        self.mainLayout.addWidget(self.changeBrowser, 2, 1)
        self.mainLayout.addWidget(self.runButton, 3, 1)
        self.mainLayout.addWidget(self.table, 0, 0, 0, 1)
        self.calibrationButton.clicked.connect(self.calibrationButtonClicked)
        self.addSubhectButton.clicked.connect(self.addButtonClicked)
        self.changeBrowser.clicked.connect(self.changeBrowserButtonClicked)
        self.runButton.clicked.connect(self.runButtonClicked)
        self.widget = QWidget()
        self.widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("MoodleBot")

    def addButtonClicked(self):
        self.w = AddLectureWidget()
        self.w.show()
        self.checkRunCondition()

    def runButtonClicked(self):
        pass

    def calibrationButtonClicked(self):
        self.w = CalibrationWidget()
        self.w.show()
        self.checkRunCondition()

    def changeBrowserButtonClicked(self):
        self.w = ChangeBrowserName()
        self.w.show()
        self.checkRunCondition()

    def checkRunCondition(self):
        global __runnable
        if len(lectures) > 0 and browsername != "" and coordinates > 0:
            __runnable = True
            self.runButton.setEnabled(True)
        else:
            __runnable = False
            self.runButton.setEnabled(False)


class CalibrationWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.layout = QtWidgets.QGridLayout()
        self.stageLabel = QLabel("Stage")
        self.coordinatesLabel = QLabel("X:n Y:n")
        self.changeButton = QPushButton()
        self.changeButton.setText("Change")
        self.changeButton.clicked.connect(self.changeButtonClicked)
        self.nextButton = QPushButton()
        self.nextButton.setText("Next")
        self.nextButton.clicked.connect(self.nextButtonClicked)
        self.layout.addWidget(self.stageLabel, 0, 0)
        self.layout.addWidget(self.coordinatesLabel, 1, 0)
        self.layout.addWidget(self.changeButton, 2, 0)
        self.layout.addWidget(self.nextButton, 2, 1)
        self.setLayout(self.layout)
        calibration.setClick()
        self.coordinatesLabel.setText(f'X: {calibration.xClick} Y: {calibration.yClick}')
        self.setWindowTitle("MoodleBot | CLick Calibration")

    def nextButtonClicked(self):
        if calibration.stage < 12:
            self.stageLabel.setText(calibration.stageText[calibration.stage])
            calibration.nextStage()
            calibration.setClick()
            self.coordinatesLabel.setText(f'X: {calibration.xClick} Y: {calibration.yClick}')
        elif calibration.stage == 12:
            calibration.stage = calibration.stage + 1
            self.nextButton.setText("Close")
            self.changeButton.setEnabled(False)
        else:
            self.close()

    def changeButtonClicked(self):
        calibration.setClick()
        self.coordinatesLabel.setText(f'X: {calibration.xClick} Y: {calibration.yClick}')


class AddLectureWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QGridLayout()
        self.label = QLabel()
        self.label.setText("Input lecture widget")
        self.labelStartLecture = QLabel()
        self.labelStartLecture.setText("Time of start")
        self.input = QtWidgets.QLineEdit()
        self.timerStart = QtWidgets.QTimeEdit()
        self.submitButton = QPushButton()
        self.submitButton.setText("Submit")
        self.submitButton.clicked.connect(self.submitButtonClicked)
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.input, 1, 0)
        self.layout.addWidget(self.labelStartLecture, 2, 0)
        self.layout.addWidget(self.timerStart, 3, 0)
        self.layout.addWidget(self.submitButton, 4, 0)
        self.setLayout(self.layout)
        self.setWindowTitle("MoodleBot | Add lecture")

    def submitButtonClicked(self):
        lectures.append(structures.Subject(self.input.text(), self.timerStart.time()))

class ChangeBrowserName(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QGridLayout()
        self.input = QtWidgets.QLineEdit()
        self.button = QPushButton()
        self.button.clicked.connect(self.buttonClicked)
        self.button.setText("Submit")
        self.layout.addWidget(self.input, 0, 0)
        self.layout.addWidget(self.button, 1, 0)
        self.setLayout(self.layout)
        self.setWindowTitle("MoodleBot | Type browser name")

    def buttonClicked(self):
        pass


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
