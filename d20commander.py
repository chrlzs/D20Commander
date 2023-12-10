import random
import re

def roll_dice(dice_notation):
    # Parse the dice notation
    match = re.match(r"""
        (\d+)      # Number of dice
        d          # Separator
        (\d+)      # Number of faces
        (          # Optional modifier
            [+-]?  # Sign
            (\d+)  # Modifier value
        )?
        (          # Optional exploding dice
            !
        )?
    """, dice_notation, re.VERBOSE)

    if not match:
        print("Invalid dice notation. Please use the format 'NdM' or 'NdM+X' or 'NdM-X'.")
        return None

    num_dice = int(match.group(1))
    num_faces = int(match.group(2))
    modifier = int(match.group(3)) if match.group(3) else 0
    exploding = bool(match.group(4))

    # Roll the dice
    rolls = []
    for _ in range(num_dice):
        while True:
            roll = random.randint(1, num_faces)
            rolls.append(roll)
            if not exploding or roll < num_faces:
                break

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
