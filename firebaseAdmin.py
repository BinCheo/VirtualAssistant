import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from time import sleep
import threading
import pyautogui

# Fetch the service account key JSON file contents
cred = credentials.Certificate('thanhbinhtruong-firebase-adminsdk-jt6r5-ec531bc3d5.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
  'projectId': 'thanhbinhtruong',
})

db = firestore.client()
keyboard = ''
def callCMD(keyword):
    if keyword == 'a':
        print("Vao")
        pyautogui.typewrite(['win'])
    else:
        print("nhu cc")
        


# Create a callback on_snapshot function to capture changes
def myOn_snapshot(col_snapshot, changes, read_time):
    
    for change in changes:
        if change.type.name == 'ADDED':
            print(f'New city: {change.document.to_dict()}')
            keyboard = change.document.to_dict()
            t1 = threading.Thread(target=callCMD(keyboard['key']))
            t1.start()
        elif change.type.name == 'MODIFIED':
            print(f'Modified city: {change.document.to_dict()}')
            keyboard = change.document.to_dict()
            t1 = threading.Thread(target=callCMD(keyboard['key']))
            t1.start()
        elif change.type.name == 'REMOVED':
            print(f'Removed city: {change.document.to_dict()}')
            keyboard = change.document.to_dict()
            t1 = threading.Thread(target=callCMD(keyboard['key']))
            t1.start()

col_query = db.collection(u'keyboard').document('device')
query_watch = col_query.on_snapshot(myOn_snapshot)

sleep(10000)

