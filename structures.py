from abc import ABC, abstractmethod

class Data(ABC):
    lectures = []
    subjects = []

    @abstractmethod
    @staticmethod
    def addSubjects(self, item):
        self.lectures.append(item)

    @abstractmethod
    @staticmethod
    def addCoordinate(self, item):
        self.subjects.append((item))

    @abstractmethod
    @staticmethod
    def getSubjects(self):
        return self.lectures

    @abstractmethod
    @staticmethod
    def getCoordinates(self):
        return self.subjects

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

class Subject:
    def __init__(self, url, time):
        self.__url = url
        self.__h = time.hour()
        self.__m = time.minute()

    def getUrl(self):
        return self.__url

    def getHour(self):
        return self.__h

    def getMinute(self):
        return self.__m
