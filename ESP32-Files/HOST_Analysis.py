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

# Get the latest 100 data values from the database
data = db.child("values").order_by_key().limit_to_last(100).get().val()

# Calculate the average of the data values
sum = 0
count = 0
for key in data:
    sum += data[key]
    count += 1
average = sum / count

print("Average of latest 100 data values:", average)
