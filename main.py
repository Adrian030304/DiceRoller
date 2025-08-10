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
    roll_history = []

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
        roll_history.append(rolling)

    # TODO: HISTORY LOGIC FOR a better handling of the data
    # To add : name, timestamp

    session['dice_type'] = f"d{dice_sides}"
    session['rolls'] = roll_history
    session['total'] = sum(roll_history)
    records.append(session)

    print(f"Thank you for rolling.")

    ask_again = input("Do you want to roll again (y/n)? ")
    if ask_again.lower() != 'y':
            break


# Your throws : dx, dy, dz
# total rolls per throw type
# average rolls 

history_prompt = input("Do you wish to see your throwing history data? (y/n) ").lower().strip()
if history_prompt == 'y':
    print(f"The records are : ")
    data_string = ''
    aggregated = {}
    for record in records:
        dice_type = record['dice_type']
        rolls = record['rolls']
        total = record['total']
        data_string += f"{dice_type} -> Rolls: {rolls}, Rolls Total: {total}, Average: {total/len(rolls):.2f} \n" 
        if dice_type not in aggregated:
            aggregated[dice_type] = rolls
        else:
            aggregated[dice_type].extend(rolls)
    print(data_string)
    
        

    

