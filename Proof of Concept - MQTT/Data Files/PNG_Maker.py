# This file will read a .txt file, plot the values of the data and save an svg of the plot 
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


tempatureList = []  # Create an empty list
timeList = []  # Create an empty list



# Open the text file for reading
#/Proof of Concept - MQTT/
with open('static/dataFile1.txt', 'r') as file:
    # Read the last 20 lines of the file
    lines = file.readlines()[-20:]


for i in range(20):
    parts = lines[i].split(" ")
    tempatureList.append(float(parts[0]))
    timeList.append(parts[1])
    
# # Plot the data
plt.figure(figsize=(13,3))
plt.plot(timeList, tempatureList)

# Add labels and title
plt.xlabel("Tempature (Degrees C)")
plt.ylabel("Time (Hr : Min)")
plt.title("Tempature of Lab")

# Show the plot
plt.savefig("static/plot1.png")
plt.show()





