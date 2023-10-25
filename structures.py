import json


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Point):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


class Subject:
    def __init__(self, url, hour, minute):
        self.url = url
        self.hour = hour
        self.minute = minute


class SubjectEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Subject):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


class Browser:
    def __init__(self, name):
        self.name = name


class BrowserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Browser):
            return obj.name
        return json.JSONEncoder.default(self, obj)