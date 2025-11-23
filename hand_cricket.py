import random
import time


# Dictionary for bowlers and their styles
BOWLER_LIST = {
    "Jasprit Bumrah": "Right-arm Fast",
    "Rashid Khan": "Right-arm Leg Spin",
    "Mitchell Starc": "Left-arm Fast",
    "Shaheen Afridi": "Left-arm Fast",
    "Kagiso Rabada": "Right-arm Fast",
    "Pat Cummins": "Right-arm Fast",
    "Wanindu Hasaranga": "Right-arm Leg Spin",
    "Trent Boult": "Left-arm Fast-Medium",
    "Ravichandran Ashwin": "Right-arm Off Spin",
    "Kuldeep Yadav": "Left-arm Chinaman"
}

COMMENTARY = {
    1: [
        "Just a quick single, nicely pushed into the gap.",
        "Tucked away to leg for a single.",
        "Good, quick running. That's one more.",
        "He's off the mark with a single.",
        "Pushed down to long-on for one."
    ],
    2: [
        "Good running, they come back for the second.",
        "Well placed, and they'll get two for it.",
        "Pushed into the deep, they hurry back for a comfortable two.",
        "A brisk couple of runs."
    ],
    3: [
        "Three runs, well placed into the outfield.",
        "That's excellent running! They'll pick up three.",
        "Finds the gap in the outfield, and they run hard for three."
    ],
    4: [
        "FOUR! Oh, that's hit right across cover for a brilliant boundary!",
        "FOUR! Smashed through the covers!",
        "Finds the gap! That's a boundary!",
        "Pulled away! One bounce and over the ropes for FOUR!",
        "Elegant drive! Races away to the boundary."
    ],
    5: [
        "FIVE RUNS! That's unusual, possibly overthrows!",
        "It's chaos in the field! They run four, and get an overthrow! That's five!",
        "FIVE! A misfield in the deep and they just keep running!"
    ],
    6: [
        "SIX! That's massive! Cleared the ropes with ease!",
        "SIX! Straight back over the bowler's head!",
        "Into the stands! That's a maximum!",
        "Gone! He's hit that a mile! SIX RUNS!",
        "What a shot! That's sailed into the crowd for SIX!"
    ]
}


OUT_COMMENTARY = [
    "CAUGHT BEHIND! A faint edge and the keeper takes it!",
    "BOWLED 'EM! Cleaned him up, right through the gate!",
    "LBW! That's plumb! The umpire's finger goes up!",
    "STUMPED! Quick hands from the keeper, he was out of his crease!",
    "CAUGHT! Straight to the fielder in the deep!"
]


def get_valid_shot(prompt):
    while True:
        try:
            shot = int(input(prompt))
            if 1 <= shot <= 6:
                return shot
            else:
                print("Invalid input! Please enter a number between 1 and 6.")
        except ValueError:
            print("That's not a number! Please enter a number between 1 and 6.")

def do_toss():

    print("--- Let's Toss! ---")

    user_choice = ""
    while user_choice not in ['heads', 'tails']:
        user_choice = input("Choose heads or tails: ").lower()

    toss_result = random.choice(['heads', 'tails'])
    print(f"The coin landed on...!")
    time.sleep(3)
    print(toss_result)

    if user_choice == toss_result:
        print("You won the toss!")
        decision = ""
        while decision not in ['bat', 'bowl']:
            decision = input("What do you want to do? (bat/bowl): ").lower()
        if decision == 'bat':
            return 'user', 'computer'
        else:
            return 'computer', 'user'
    else:
        print("The computer won the toss.")
        decision = random.choice(['bat', 'bowl'])
        print(f"The computer has decided to {decision}.")
        time.sleep(1)
        if decision == 'bat':
            return 'computer', 'user'
        else:
            return 'user', 'computer'


def play_innings(batting_team, bowling_team, target=None):
    
    total_score = 0
    wickets_left = 1
    overs = 0
    balls_in_over = 0
    current_over_balls = [] # Stores scores for the over summary
    current_bowler = ""
    
    # Set the batter's name for display
    batter_name = "You" if batting_team == 'user' else "Computer"

    while wickets_left > 0:
        
        # --- Start of Over Logic ---
        if balls_in_over == 0:
            # Print the summary of the *previous* over
            if overs > 0:
                print("\n" + "="*30)
                print(f"--- End of Over {overs} ---")
                print(f"**Score: {total_score} / {1 - wickets_left}**")
                print(f"Batter: {batter_name}")
                print(f"Bowler: {current_bowler}")
                # Display the score of each ball in the over
                print(f"Over: {' '.join(current_over_balls)}")
                print("="*30)
                time.sleep(2) # Pause to read the summary

            # Start a new over
            overs += 1
            current_over_balls = [] # Reset for the new over
            
            # Select a new random bowler
            current_bowler, bowler_style = random.choice(list(BOWLER_LIST.items()))
            
            print(f"\n--- Over {overs} ---")
            print(f"**New Bowler: {current_bowler}**")
            print(f"Bowling Style: {bowler_style}")
            if target:
                print(f"Target: {target} | Need {target - total_score} to win")

        # --- Get Shots ---
        print(f"\nOver {overs}, Ball {balls_in_over + 1}")
        
        if batting_team == 'user':
            user_shot = get_valid_shot("Your shot (1-6): ")
            comp_shot = random.randint(1, 6)
            print(f"You played: {user_shot}")
            print(f"Bowler played: {comp_shot}")
            batter_shot, bowler_shot = user_shot, comp_shot

        else:
            user_shot = get_valid_shot(f"Your bowl : ")
            comp_shot = random.randint(1, 6)
            print(f"You (Bowler) played: {user_shot}")
            print(f"{batter_name} (Batter) played: {comp_shot}")
            batter_shot, bowler_shot = comp_shot, user_shot

        time.sleep(1)


        if batter_shot == bowler_shot:
            # OUT!
            wickets_left = 0
            current_over_balls.append("W") # 'W' for Wicket
            print("\n" + "!"*40)

            print(f"--- {random.choice(OUT_COMMENTARY)} ---")
            print(f"** {batter_name} depart for a score of {total_score}! **")
            print("!"*40)
            balls_in_over += 1 # Count the wicket ball
            break # End the innings
        else:
            # SCORE
            runs = batter_shot
            total_score += runs
            current_over_balls.append(str(runs))
            
            # Display a random commentary for the specific shot
            commentary_list = COMMENTARY.get(runs, ["..."]) # Get the list of commentaries
            selected_commentary = random.choice(commentary_list) # Pick one at random
            print(f"Commentary: {selected_commentary}")

            if target and total_score > target:
                print(f"\n{batter_name} has passed the target!")
                break

            balls_in_over += 1


        # --- End of Over ---
        if balls_in_over == 6:
            balls_in_over = 0 # This will trigger the new over logic at the start of the next loop
    
    # --- End of Innings Summary ---
    print(f"\n--- End of {batting_team.title()}'s Innings ---")
    print(f"Final Score: {total_score} / {1 - wickets_left}")

    overs_display = f"{overs - 1}.{balls_in_over}" if balls_in_over != 0 else f"{overs}.0"
    if overs == 1 and balls_in_over == 0: overs_display = "1.0" # Fix for 1-over innings
        
    print(f"Overs: {overs_display}")
    
    # If the innings ended mid-over, show the final over's score
    if balls_in_over != 0:
        print(f"Final Over: {' '.join(current_over_balls)}")
        
    return total_score


def main():
    print("=======================================")
    print("        Let's play Hand Cricket!   ")
    print("=======================================")
    
    bats_first, bowls_first = do_toss()
    
    print(f"\n{bats_first.title()} will bat first.")
    
    # --- 1st Innings ---
    print("\n" + "-"*15 + " 1st Innings " + "-"*15)
    score_1 = play_innings(bats_first, bowls_first)
    
    target = score_1 + 1
    print(f"\n--- End of 1st Innings ---")
    print(f"{bats_first.title()} scored {score_1}.")
    print(f"{bowls_first.title()} needs {target} runs to win.")
    
    input("\nPress Enter to start the 2nd Innings...")
    
    # --- 2nd Innings ---
    print("\n" + "-"*15 + " 2nd Innings " + "-"*15)
    score_2 = play_innings(bowls_first, bats_first, target=target)

    # --- Determine Winner ---
    print("\n=======================================")
    print("           --- Match Over ---          ")
    print("=======================================")
    print(f"1s Innings Score ({bats_first.title()}): {score_1}")
    print(f"2nd Innings Score ({bowls_first.title()}): {score_2}")
    
    if score_2 > score_1:
        print(f"\n** {bowls_first.title()} wins! **")
    elif score_1 > score_2:
        print(f"\n** {bats_first.title()} wins! **")
    else:
        print("\n** The match is a TIE! **")

# --- Run the game ---
if __name__ == "__main__":
    main()