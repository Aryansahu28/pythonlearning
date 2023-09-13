# Get the current time in hours from the user
current_time = int(input("Enter the current time (in hours): "))

# Get the number of hours to wait for the alarm from the user
hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the alarm time using modulo 24
alarm_time = (current_time + hours_to_wait) % 24


# Print the alarm time
print(f"The alarm will go off at {alarm_time}:00")
