# Get user input for initial velocity, final velocity, and time
initial_velocity = float(input("Enter the initial velocity (m/s): "))
final_velocity = float(input("Enter the final velocity (m/s): "))
time = float(input("Enter the time taken (s): "))

# Calculate acceleration
acceleration = (final_velocity - initial_velocity) / time

# Display the result
print("The acceleration is", acceleration, "m/s^2")