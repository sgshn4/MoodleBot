import point
stageText = ["Click start Windows button.",
             "Type your browser name.",
             "Click on result of search.",
             "Open VSU site.",
             "Login in.",
             "Open lecture to connect.",
             "Click \"Connect\" button.",
             "Click to turn on the sound button.",
             "Click menu button.",
             "Click \"Leave conference\" button.",
             "Click to URL bar.",
             "Saved. Now you can add subjects to connect."]
stage = 0
coordinates = []

#1 2 3 4 11
def nextStage():
    global stage
    global coordinates
    if (stage != 1 or stage != 2 or stage != 3 or stage != 4 or stage != 11):
        coordinates.append(point.Point())
        stage = stage + 1
