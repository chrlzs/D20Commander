import random
import re

def roll_dice(dice_notation):
    # Parse the dice notation (e.g., "2d6" or "1d20+5")
    match = re.match(r'(\d+)d(\d+)([+-]\d+)?', dice_notation)
    if not match:
        print("Invalid dice notation. Please use the format 'NdM' or 'NdM+X' or 'NdM-X'.")
        return None

    num_dice = int(match.group(1))
    num_faces = int(match.group(2))
    modifier = int(match.group(3)) if match.group(3) else 0

    # Roll the dice
    rolls = [random.randint(1, num_faces) for _ in range(num_dice)]

    # Calculate the total
    total = sum(rolls) + modifier

    return rolls, total

def main():
    while True:
        user_input = input("Enter dice notation (e.g., '2d6' or '1d20+5'), or 'exit' to quit: ").lower()

        if user_input == 'exit':
            break

        result = roll_dice(user_input)
        if result is not None:
            rolls, total = result
            print(f"Rolls: {rolls}")
            print(f"Total: {total}")

if __name__ == "__main__":
    main()
