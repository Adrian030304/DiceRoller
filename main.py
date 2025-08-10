import random
from collections import defaultdict
from datetime import datetime
from statistics import mode

# Records of the dice rolls and storage for save/load logic
records = []

# new roll format for dice XdN x-how many rolls n-sides per die
# Create a logic to select the rolles and sides of the die while adhering to a format
# format Ndx

print("="*50)
print("Welcome to a small Dice Roller game!")
print("You can throw roll dices typing (NdX).")
print("---- N- number of throws. ----")
print("---- X- number of dice sides. ----")


# main menu with choices
options = ["Roll dice",
           "View roll history",
           "view Statistics",
           "Save session",
           "Load session",
           "Quit"]

while True:
    print("="*50)
    for idx, option in enumerate(options):
        print(f"{idx + 1}. {option}")
    option_choice = input("Please choose an option: ")
    if option_choice == '1':
        print("="*50)
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

            # HISTORY LOGIC FOR a better handling of the data
            # To add : name, timestamp

            session['dice_type'] = f"d{dice_sides}"
            session['rolls'] = roll_history
            session['total'] = sum(roll_history)
            session['time'] = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
            records.append(session)

            print(f"Thank you for rolling.")

            ask_again = input("Do you want to roll again (y/n)? ")
            if ask_again.lower() != 'y':
                    break
            print("="*50)

    elif option_choice == '2':
        # Your throws : dx, dy, dz
        # total rolls per throw type
        # average rolls 

        history_prompt = input("Do you wish to see your throwing history data? (y/n) ").lower().strip()
        if history_prompt == 'y':
            print(f"The records are : ")
            data_string = ''
            for record in records:
                roll_time = record['time']
                dice_type = record['dice_type']
                rolls = record['rolls']
                total = record['total']
                average_rolls = f"{total/len(rolls):.2f}"
                data_string += f"| {roll_time} | {dice_type} -> Rolls: {rolls} | Total: {total} | Avg: {average_rolls}\n" 
            print(data_string)
    elif option_choice == '3':
        # stats part, to implement a staticical view of the dice rolls along with the aggregated type , also on save/load to 

        stats_prompt = input("Do you want to see your throw statistics (y/n)? ").lower().strip()
        if stats_prompt != 'y':
            print("Going back to the main menu..")
        elif not records:
            print("The dice are silent... no rolls to show.\n")
        else:
            aggregate_dices = defaultdict(list)
            for record in records:
                aggregate_dices[record['dice_type']].extend(record['rolls'])
            print(f"Here's a summary of your dice rolling stats so far: \n")
            for agg_dice in aggregate_dices:
                agg_roll = aggregate_dices[agg_dice]
                print(f"Dice Type: {agg_dice}")
                print(f"  Rolls Sum: {sum(agg_roll)}")
                print(f"  Average Roll: {sum(agg_roll)/len(agg_roll):.2f}")
                print(f"  Min Rolled number: {min(agg_roll)}")
                print(f"  Max Rolled number: {max(agg_roll)}")
                print(f"  Most Frequent rolled number: {mode(agg_roll)} \n")
            print(f"That's all for your stats — happy rolling!")
            print('='*50)

    elif option_choice == str(len(options)):
        print("Quitting...")
        break
    else:
        print("Invalid option.")