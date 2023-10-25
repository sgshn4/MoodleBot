import json
import structures


def saveToFile(name, value, cls):
    with open(name, "w") as file:
        json.dump(value, file, cls=cls)
        file.close()


def readFromFile(name):
    with open(name, "r") as file:
        result = json.load(file)
        file.close()
        return result


def configurePoints():
    string = readFromFile("coordinates.json")
    result = []
    for i in range(len(string)):
        result.append(structures.Point(string[i].get("x"), string[i].get("y")))
    return result


def configureLectures():
    string = readFromFile("lectures.json")
    result = []
    for i in range(len(string)):
        result.append(structures.Subject(string[i].get("url"), string[i].get("hour"), string[i].get("minute")))
    return result


def configureBrowser():
    string = readFromFile("browser.json")
    return string
