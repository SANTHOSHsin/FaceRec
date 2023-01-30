import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://sandyface-804db-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "12345":
        {
            "name": "Santhosh",
            "major": "IT std",
            "starting_year": 2021,
            "total_attendance": 9,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
        "54321":
        {
            "name": "Samual;",
            "major": "IT std",
            "starting_year": 2021,
            "total_attendance": 1,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "108481":
        {
            "name": "Azhar Alauddin",
            "major": "Informatics",
            "starting_year": 20178,
            "total_attendance": 4,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

# JSON in Python is Dictionary
for key, value in data.items():
    ref.child(key).set(value)