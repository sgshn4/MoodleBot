class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class Subject:
    def __init__(self, url, time):
        self.url = url
        self.h = time.hour()
        self.m = time.minute()

    def getUrl(self):
        return self.url

    def getHour(self):
        return self.h

    def getMinute(self):
        return self.m