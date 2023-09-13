import random

# Define the child's rights
child_rights = {
    "1": "The right to education",
    "2": "The right to play and rest",
    "3": "The right to be protected from harm",
    "4": "The right to express your opinion",
}

def display_rights():
    print("\nChild's Rights:")
    for key, value in child_rights.items():
        print(f"{key}: {value}")

def play_game():
    print("Welcome to the Child's Rights Learning Game!")
    print("Let's learn about some of your rights.")
    
    display_rights()

    while True:
        # Choose a random right to ask about
        random_right = random.choice(list(child_rights.keys()))
        print("\nHere's a question about your rights:")
        print(f"What is the right numbered '{random_right}'?")
        
        user_input = input("Your answer (or 'q' to quit): ").strip().lower()

        if user_input == 'q':
            print("\nThank you for playing! Goodbye!")
            break

        if user_input == random_right:
            print("That's correct! You know your rights!")
        else:
            print("Oops! That's not the right number. Try again.")

if __name__ == "__main__":
    play_game()
