def find_note_combinations(target_price, notes_available, current_combination=[]):
    if target_price == 0:
        # Found a valid combination, print it
        print(current_combination)
        return

    if target_price < 0 or not notes_available:
        # Either we've exceeded the target_price or we've run out of note options
        return

    # Explore two possibilities for the current note denomination:
    # 1. Use one note of the current denomination
    find_note_combinations(target_price - notes_available[0], notes_available, current_combination + [notes_available[0]])

    # 2. Move to the next denomination
    find_note_combinations(target_price, notes_available[1:], current_combination)

# Example usage:
target_price = 50
notes_available = [10, 20, 50]  # Denominations available
find_note_combinations(target_price, notes_available, [])
