import random

# new roll format for dice XdN x-how many rolls n-sides per die
# TODO: Create a logic to select the rolles and sides of the die while adhering to a format


# TODO: Create history session logic
records = []

while True:
    session = {}
    history_stack = []

    try:
        rolls_amount = input("How many times do you want to roll? ")
        if rolls_amount and not rolls_amount.isdigit():
            raise TypeError("You can only input numbers")
        if int(rolls_amount) < 1:
            raise ValueError("Negative Numbers are not allowed. Try again.")
    except TypeError as e:
        print(f"Warning: {e}. Only digits are allowed")
        continue
    except ValueError as err:
        print(f"Warning: {err}. The minimum value is 1.")
        continue

    dice_sides = input("How many sides do you choose? ")
    if not dice_sides.isdigit():
        continue

    print(f"Throw amount: {rolls_amount}")
    print(f"Dice sides: {dice_sides}")

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

    ask_again = input("Do you want to roll again (y/n)? ")
    if ask_again.lower() != 'y':
            break

print(f"Thank you for rolling.")
for i in range(len(history_stack)):
    print(f"{str(i + 1) + '.Roll: ' + str(history_stack[i])}")
total_dice_amount = sum(history_stack)
print(f"Your total dice score is: {total_dice_amount}")
print(f"The records are : {records}")
history_stack.clear()
