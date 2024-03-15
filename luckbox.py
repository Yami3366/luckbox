import random
# 
# SY23120012457
# Skills Bootcamp in Software Engineering (Fundamentals)
# Task 9 - Defensive Programming - Error Handling
# 10-015 Defensive Programming - Error Handling
# Pactical Task 2
# luckbox.py
# Write a program with two compilation errors, a runtime error and a logical error.
# Next to each error, add a comment that explains what type of error it is and why it occurs.
# 3-Feb-2024 the last update.
# 20-Feb-2024 Version update 
# 1. Add the default value of the prize to test the program 
# 2. coding style referece  https://peps.python.org/pep-0008/#comments and revised
# 3. The program interface  logic and operations impove
# 21-Feb-2024 validate input prize_count and participant_count

# ================== Types of Errors ==================
# There are 3 types of errors:
# - <1>Compilation or syntax errors (2)
# - <2>Runtime errors (1)

# (code with <1.1> Compilation or syntax errors)
# print(r"   )\ )        (    ( /(  ( /(     (  ( /( ( /(      ") 
# invalid escape sequence '\/'

# (fixed code <1.1>)
# print(r string)Raw Strings Ignore Escape Character Sequences 
# Display welcome message
print("\n")
print(r"Welcome to...")
print(r"       (                   )     )           )       ")
print(r"   )\ )        (    ( /(  ( /(     (  ( /( ( /(      ") 
print(r"  (()/(   (    )\   )\()) )\())  ( )\ )\()))\())     ")    
print(r"   /(_))  )\ (((_)|((_)\ ((_)\   )((_((_)\((_)\      ") 
print(r"  (_)) _ ((_))\___|_ ((___ ((_) ((_)_  ((___((_)     ") 
print(r"  | | | | | ((/ __| |/ /\ \ / /  | _ )/ _ \ \/ /     ") 
print(r"  | |_| |_| || (__  ' <  \ V /   | _ | (_) >  <      ") 
print(r"  |____\___/  \___|_|\_\  |_|    |___/\___/_/\_\     ")   
print(r".  . . . . . . . . . . . . . . . . . . . . . . . . . ")

# Display the list of prizes total participants
print("\n")
     
def validate_participant_count(participant_count, prize_count):
    return prize_count > participant_count

# # Get the number of prize_count in the lottery from the user and convert it to an integer
prize_count = input("Enter How many prizes : ")
while not prize_count.isdigit():
    print("Error: Please enter a valid number for prizes count.")
    prize_count = input("Enter How many prizes : ")
prize_count = int(prize_count)

# Get the number of participants in the lottery from the user and convert it to an integer
participant_count = input("how many people participating in the lottery : ")
while not participant_count.isdigit():
    print("Error: Please enter a valid number for participant count.")
    participant_count = input("how many people participating in the lottery : ")
participant_count = int(participant_count)

print("\n")
if validate_participant_count(participant_count, prize_count):
    print("The number of prizes exceeds the number of participants")
    print("The Lucky box will stop at the last prize.\n")
else:
    None

# Initialize an empty list to store prizes
prizes = []

# Loop through the range of the number of prizes
for i in range(prize_count):
    # Get user input for each prize with a default value
    default_prize = f"Prize {i+1}"
    user_input = input(f"Enter prize {i+1} (default: {default_prize}): ") or default_prize

    # Append the user input to the list of prizes
    prizes.append(user_input)

# Display the list of prizes
print("\nThe following is the list of prizes for this draw:\n")
for idx, prize in enumerate(prizes, start=1):
    print(f"{idx}. {prize}")

# Assigning the value of participant_count to the variable participant
    
participant = participant_count
print("\n")
# Define a function named luckybox that takes two parameters: 
# prizes (a list of prizes) and participant (the number of participants)
def luckybox(prizes, participant):
    
    # (code with <1.2> runtime error)
    # print("The lottery begins today with" + len(prizes) + "prizes. Here's the list of prizes.")
    # TypeError: can only concatenate str (not "set") to str
    
    # # (fixed code <1.2>) 
    # using Python f-strings
    print(f"The lottery begins today with {len(prizes)} prizes.")
    print("Here's the list of prizes.\n")
    print(f"There are {participant} participants.\n")
     
    x = 0
    for prize in prizes:
        x = x + 1
        print(f"{x}. {prize}\n")
    
    # # pause programm wait user action
    wait = input("👆👆👆Press ENTER to draw START  winner👆👆👆\n")

    # Set to store winners
    winners = set()

    # (code with <3>.Logical errors)
    ''' In the lucky box program, with 5 prizes and 4 participants, 
        encountering a situation where the program hangs 
        when awarding the fourth prize is indicative of a logical error.
        '''

    x = 0
    # Loop through each prize to draw winners
    for prize in prizes:
        x = x + 1

        # (fixed code <3>.Logical errors)
        # Verify if all participants in the lottery have been selected.
        if len(winners) == participant:
            print("Not enough people, the draw ends")
            break

        print(f"{x}. Prize: {prize}")        

        # Draw a winner for the current prize
        while True:
            draw = random.randint(1, participant)
            
            # Check if the draw is unique (not a previous winner)
            if draw not in winners:
                winners.add(draw)
                break  # Exit the loop when a unique winner is found

        print(f".----------------------------------------------------.")  
        print(f"  .------------------------------------------------.  ") 
        print(f"    .                                            .    ")  
        print(f"      .                                        .      ")
        print(f"        .                                    .        ")
        print(f"           \033[1;41m    Lottery Ticket Number {draw}     \033[m        ") 
        print(f"             wins {prize}")
        print(f"        .                                    .") 
        print(f"      .                                        .      ")
        print(f"    .                                            .    ")  
        print(f"| '------------------------------------------------' |")
        print(f" '---------------------------------------------------'")
                                                                        
        print("\n")
        # pause programm wait user action
        wait = input("👆👆👆Press Enter to draw the next lucky winner👆👆👆\n")
        # print("\n")

    # Display completion message
    print("\nLottery draw completed. Thank you for participating!")
    print("\n")

luckybox(prizes, participant)

# Test Case 1
# Enter How many prizes : 5
# how many people participating in the lottery : 13
# Manual input below data item . If not use defailt Prize 1..
# iPhone 15 Pro
# Apple iPad 10.9
# Xbox Series X
# KODAK Mini Portable Photo Printer
# Garmin Forerunner 255 GPS Watch





