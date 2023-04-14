# This file will read a .txt file, plot the values of the data and save an svg of the plot 
import matplotlib.pyplot as plt

# Open the text file for reading
with open('/Proof of Concept - MQTT/dataFile1.txt', 'r') as file:
    # Read the last 20 lines of the file
    lines = file.readlines()[-20:]

# Convert each line to a float and store in a list
data = [float(line.strip()) for line in lines]

# Plot the data using Matplotlib
plt.plot(data)
plt.ylabel('Tempature (Degrees C)')
plt.title('Tempature of Lab')
plt.savefig('plot.png')


plt.show()

