import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from time import sleep
import threading
import pyautogui

# Fetch the service account key JSON file contents
cred = credentials.Certificate('thanhbinhtruong-firebase-adminsdk-jt6r5-aef46fcacf.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
  'projectId': 'thanhbinhtruong',
})

db = firestore.client()
# doc_ref = db.collection(u'users').document(u'alovelace')
# doc_ref.set({
#     u'first': u'Ada',
#     u'last': u'Lovelace',
#     u'born': 1815
# })

# doc_ref = db.collection(u'users').document(u'alovelace')

# doc = doc_ref.get()
# if doc.exists:
#     print(f'Document data: {doc.to_dict()}')
# else:
#     print(u'No such document!')

# db = firestore.Client()
# [START listen_for_changes]

def callCMD(keyword):
    if keyword == 'a':
        pyautogui.typewrite(['windows'])
    else:
        print("nhu cc")

# Create an Event for notifying main thread.
delete_done = threading.Event()

# Create a callback on_snapshot function to capture changes
def on_snapshot(col_snapshot, changes, read_time):
    global keyboard
    for change in changes:
        if change.type.name == 'ADDED':
            print(f'New city: {change.document.to_dict()}')
            keyboard = change.document.to_dict()
            callCMD(keyboard['key'])
        elif change.type.name == 'MODIFIED':
            print(f'Modified city: {change.document.to_dict()}')
            keyboard = change.document.to_dict()
            keyboard['key']
        elif change.type.name == 'REMOVED':
            print(f'Removed city: {change.document.to_dict()}')
            keyboard = change.document.to_dict()
            keyboard['key']
            delete_done.set()

col_query = db.collection(u'keyboard').document('device')

# Watch the collection query
query_watch = col_query.on_snapshot(on_snapshot)

sleep(10000)

delete_done.wait(timeout=60)

