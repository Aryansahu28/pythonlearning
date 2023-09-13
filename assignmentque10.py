# Get the starting day number from the user (0 for Sunday to 6 for Saturday)
starting_day = int(input("Enter the starting day number (0 for Sunday, 1 for Monday, ..., 6 for Saturday): "))

# Get the length of your stay (number of nights) from the user
length_of_stay = int(input("Enter the length of your stay (number of nights): "))

# Calculate the day of the week you will return on
return_day = (starting_day + length_of_stay) % 7

# Define a list of day names
day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Print the day of the week you will return on
print(f"You will return home on a {day_names[return_day]}.")
