# Import libraries
import random

# Create lists
A_East = []
A_West = []
B_South = []

# Create loop to fill lists
for i in range(0, 10):
    A_East.append(random.randint(0, 1))
    A_West.append(random.randint(0, 1))
    B_South.append(random.randint(0, 1))

# Create a variable to control traffic light
X = 1

# Create a loop to control traffic
while True:
    # Initialize variables
    A_East_waiting_time = 0
    A_West_waiting_time = 0
    B_South_waiting_time = 0

    # Calculate waiting time for each list
    for i in range(0, len(A_East)):
        if A_East[i] == 1:
            A_East_waiting_time += 1
        if A_West[i] == 1:
            A_West_waiting_time += 1
        if B_South[i] == 1:
            B_South_waiting_time += 1

    # Calculate combined waiting time for A lists
    combined_A_waiting_time = A_East_waiting_time + A_West_waiting_time

    # Compare combined waiting time
    if combined_A_waiting_time * 2 > B_South_waiting_time:
        X = 0
    else:
        X = 1

    # Fill lists
    for i in range(0, len(A_East)):
        if X == 1:
            A_East[i] = random.randint(0, 1)
            A_West[i] = random.randint(0, 1)
            B_South[i] = 1
        else:
            A_East[i] = random.randint(0, 1)
            A_West[i] = random.randint(0, 1)
            B_South[i] = 0

    # Print lists
    print("A_East: ", A_East)
    print("A_West: ", A_West)
    print("B_South: ", B_South, "\n")