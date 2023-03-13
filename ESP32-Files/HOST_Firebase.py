import pyrebase

# Configure Firebase credentials
config = {
  "apiKey": "YOUR_API_KEY",
  "authDomain": "YOUR_AUTH_DOMAIN",
  "databaseURL": "YOUR_DATABASE_URL",
  "projectId": "YOUR_PROJECT_ID",
  "storageBucket": "YOUR_STORAGE_BUCKET",
  "messagingSenderId": "YOUR_SENDER_ID",
  "appId": "YOUR_APP_ID",
  "measurementId": "YOUR_MEASUREMENT_ID"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(config)

# Get a reference to the database service
db = firebase.database()

# Write some data to the database
data = {"sensor": "Temp1", "temp": 30}
db.child("sensor").child("temp").set(data)

# Read some data from the database
user = db.child("users").child("temp").get().val()
print(user) # {"users": "Temp1", "temp": 30}
