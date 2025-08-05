import random

# new roll format for dice XdN x-how many rolls n-sides per die
# TODO: Create a logic to select the rolles and sides of the die while adhering to a format
# format Ndx

print("Welcome to dice roller. You can throw roll dices typing (NdX).")
print("N- number of throws.")
print("X- number of dice sides.")

# TODO: Create history session logic


records = []

while True:
    
    session = {}
    history_stack = []

    while True:
        try:
            dice_roll_choice = input("Enter dice roll in the format NdX (e.g. 3d6): ")
            dice_roll_choice = dice_roll_choice.lower().strip()

            if  ('d' not in dice_roll_choice
                or len(dice_roll_choice.split('d')) != 2
                or not dice_roll_choice.split('d')[0].isdigit()
                or not dice_roll_choice.split('d')[1].isdigit()
                ):
                raise ValueError(f"This is not respecting the format (NdX) -> {dice_roll_choice}")
            
        except ValueError as err:
            print(f"Warning: {err}.")
            continue
        break

    print(f"dice_roll_choice {dice_roll_choice}")
    try:
        rolls_amount, dice_sides = dice_roll_choice.split('d')
        if int(rolls_amount) < 1 or int(dice_sides) < 1:
            raise ValueError("Negative Numbers are not allowed. Try again.")
    except ValueError as err:
        print(f"Warning: {err}. The minimum value is 1.")
        continue

    rolls_amount = int(rolls_amount)
    dice_sides = int(dice_sides)

    print(f"You threw a {rolls_amount}d{dice_sides}.")
    print(f"Throw {rolls_amount} times...")

    for _ in range(rolls_amount):
        rolling = random.randint(1,dice_sides)
        print(f"You rolled {rolling} ")
        history_stack.append(rolling)

    
    session[f"d{dice_sides}"] = history_stack
    records.append(session)

    print(f"Thank you for rolling.")
    for i in range(len(history_stack)):
        print(f"{str(i + 1) + '.Roll: ' + str(history_stack[i])}")
    total_dice_amount = sum(history_stack)
    print(f"Your total dice score is: {total_dice_amount}")

    ask_again = input("Do you want to roll again (y/n)? ")
    if ask_again.lower() != 'y':
            break
    
print(f"The records are : {records}")
history_stack.clear()
