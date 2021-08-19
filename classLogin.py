import datetime
now = datetime.datetime.now()
today = now.strftime("%A")
import webbrowser
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# print(today)

classLinks = {
    "CCN" : "https://meet.google.com/dvw-trvx-ddm", 
    "WC" : "https://meet.google.com/dvw-trvx-ddm",
    "OC" : "https://meet.google.com/rdk-zvod-auz",
    "MWR" : "https://meet.google.com/kzg-aeza-bde",
    "IVP" : "http://meet.google.com/owu-mghp-ajn",
    "PP" : "https://meet.google.com/aiv-cdec-imo",
    "IOT" : "https://meet.google.com/ayy-iqwo-vuu"
}

# my time table
timeTable = {
    "Monday" : {
        "period1" : "WC",
        "period2" : "IOT",
        "period3" : "OC",
        "period4" : "MWR",
        "period5" : "IVP",
        "period6" : "Monitoring Hour",
        "period1" : "Library",
    },
    "Tuesday" : {
        "period1" : "CCN",
        "period2" : "OC",
        "period3" : "MWR",
        "period4" : "IVP",
        "period5" : "CP-D",
        "period6" : "CP-D",
        "period7" : "Sports",
    },
    "Wednesday" : {
        "period1" : "CCN",
        "period2" : "CCN",
        "period3" : "MWR",
        "period4" : "MWR",
        "period5" : "Cultural Activities",
        "period6" : "OSA Activities",
        "period7" : "OSA Activities",
    },
    "Thursday" : {
        "period1" : "WC",
        "period2" : "IVP",
        "period3" : "CCN",
        "period4" : "IOT",
        "period5" : "MWR",
        "period6" : "IVP",
        "period7" : "IVP",
    },
    "Friday" : {
        "period1" : "OC",
        "period2" : "WC",
        "period3" : "PP-V",
        "period4" : "PP-V",
        "period5" : "Library",
        "period6" : "OSA Activities",
        "period7" : "OSA Activities",
    },
    "Saturday" : {
        "period1" : "CCN",
        "period2" : "IOT",
        "period3" : "CP-D",
        "period4" : "CP-D",
    }
}

print("Todays Time Table = ", timeTable[today])

# time table period definition
def time_in_range(start, end, current):
    """Returns whether current is in the range [start, end]"""
    return start <= current <= end
# start = datetime.time(10, 45, 0)
# end = datetime.time(11, 45, 0)
# current = datetime.datetime.now().time()
# print(time_in_range(start, end, current))

def findPeriod():
    current = datetime.datetime.now().time()
    if time_in_range(datetime.time(8, 30, 0), datetime.time(9, 30, 0), current):
        return "period1"
    elif time_in_range(datetime.time(9, 30, 0), datetime.time(10, 30, 0), current):
        return "period2"
    elif time_in_range(datetime.time(10, 30, 0), datetime.time(10, 45, 0), current):
        return "Break Time"
    elif time_in_range(datetime.time(10, 45, 0), datetime.time(11, 45, 0), current):
        return "period3"
    elif time_in_range(datetime.time(11, 45, 0), datetime.time(12, 45, 0), current):
        return "period4"
    elif time_in_range(datetime.time(12, 45, 0), datetime.time(1, 30, 0), current):
        return "Lunch Break"
    elif time_in_range(datetime.time(1, 30, 0), datetime.time(2, 30, 0), current):
        return "period5"
    elif time_in_range(datetime.time(2, 30, 0), datetime.time(3, 30, 0), current):
        return "period6"
    elif time_in_range(datetime.time(3, 30, 0), datetime.time(4, 30, 0), current):
        return "period7"
    else:
        return "No Class"

period = findPeriod()
print("Current period = ",period)
currentClass = timeTable[today][period]
print("current class = ", currentClass)
classLink = classLinks[currentClass]
print("Class Link = ", classLink)

print("opening Link in your web browser.....")
webbrowser.open(classLink, new=2)
print("Turning off Mic and Camera, please wait....")
time.sleep(6)
# turn off mic 
pyautogui.hotkey('ctrl', 'd')
pyautogui.hotkey('ctrl', 'e')

