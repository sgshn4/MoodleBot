from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel
from PyQt5 import QtWidgets, QtCore
from threading import Thread
import sys
import calibration
import structures
import utils
import time

browsername = ""
lectures = []
runnable = False


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.isRunning = True
        self.mainLayout = QtWidgets.QGridLayout()
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(1)
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
        self.updater = Thread(target=self.task)
        self.updater.start()

    def task(self):
        global lectures
        while self.isRunning:
            self.table.setRowCount(len(lectures))
            for i in range(len(lectures)):
                lectures = utils.configureLectures()
                self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(lectures[i].url))
            time.sleep(1)

    def closeEvent(self, event):
        self.isRunning = False

    def addButtonClicked(self):
        if self.checkConditions:
            self.w = AddLectureWidget()
            self.w.show()


    def runButtonClicked(self):
        if self.checkConditions():
            pass

    def calibrationButtonClicked(self):
        self.w = CalibrationWidget()
        self.w.show()

    def changeBrowserButtonClicked(self):
        self.w = ChangeBrowserName()
        self.w.show()

    def checkConditions(self):
        if len(utils.configurePoints()) > 0 and len(utils.configureLectures()) > 0 and browsername != "":
            return True


class CalibrationWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.isRunning = True
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.layout = QtWidgets.QGridLayout()
        self.stageLabel = QLabel("Welcome to calibration. Press next to start.")
        self.changeButton = QPushButton()
        self.changeButton.setText("Change")
        self.changeButton.clicked.connect(self.changeButtonClicked)
        self.nextButton = QPushButton()
        self.nextButton.setText("Next")
        self.nextButton.clicked.connect(self.nextButtonClicked)
        self.layout.addWidget(self.stageLabel, 0, 0)
        self.layout.addWidget(self.changeButton, 1, 0)
        self.layout.addWidget(self.nextButton, 1, 1)
        self.setLayout(self.layout)
        calibration.setClick()
        self.setWindowTitle("MoodleBot | CLick Calibration")

    def nextButtonClicked(self):
        if calibration.stage < 12:
            self.stageLabel.setText(calibration.stageText[calibration.stage])
            calibration.nextStage()
            calibration.setClick()
        elif calibration.stage == 12:
            calibration.stage = calibration.stage + 1
            self.nextButton.setText("Close")
            self.changeButton.setEnabled(False)
        else:
            utils.saveToFile("coordinates.json", calibration.coordinates)
            self.isRunning = False
            self.close()

    def changeButtonClicked(self):
        calibration.setClick()


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
        lectures.append(structures.Subject(self.input.text(), self.timerStart.time().hour(), self.timerStart.time().minute()))
        utils.saveToFile("lectures.json", lectures, structures.SubjectEncoder)
        self.close()



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
        browsername = structures.Browser(self.input)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
