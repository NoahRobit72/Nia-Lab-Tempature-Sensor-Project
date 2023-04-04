import sys
import matplotlib.pyplot as plt

# Initialize empty data and time lists
data = []
time = []

# Loop to get user input and plot data
while True:
    # Get user input
    user_input = input("Enter data value (or x to exit): ")

    # Check if user wants to exit
    if user_input.lower() == 'x':
        break

    # Convert input to float and append to data list
    try:
        data_value = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a number or x to exit.")
        continue

    data.append(data_value)

    # Add current time to time list
    current_time = len(data) - 1
    time.append(current_time)

    # Plot updated data and time lists
    plt.plot(time, data)

    # Add labels and title
    plt.xlabel('Time')
    plt.ylabel('Data Value')
    plt.title('Data Values Over Time')

    # Show the plot
    plt.show()

