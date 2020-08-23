# import pyautogui
# from time import sleep
# from win32api import GetSystemMetrics

# pyautogui.FAILSAFE = False
# print(pyautogui.position())
# x = GetSystemMetrics(0)
# y = GetSystemMetrics(1)
# pyautogui.typewrite(['win'])
# # pyautogui.moveTo(0, y-1, 1)
# # pyautogui.click()
# # sleep(1)
# # pyautogui.typewrite('Google Chrome')
# # sleep(1)
# # pyautogui.typewrite(['windows'])


# Import database module.
from firebase_admin import db

# Get a database reference to our posts
ref = db.reference('server/saving-data/fireblog/posts')

# Read the data at the posts reference (this is a blocking operation)
print(ref.get())
