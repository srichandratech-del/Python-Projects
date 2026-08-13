import sys

# ==========================================
# RUN THE INITIAL SCRIPT CALL
# ==========================================
print("==================================================")
print("          WELCOME TO PROJECT: ICARUS              ")
print("==================================================")
print("Emergency Alert: Deep-space research vessel hull breached!")
print("Systems failing. You must survive the lockdown protocols.\n")

print("=== EMERGENCY PROTOCOL INITIALIZED ===")

# ==========================================
# GLOBAL STATE VARIABLES
# ==========================================
Oxygen = 80
has_extinguisher = False
life_room_solved = False

# ==========================================
# GAME FUNCTIONS
# ==========================================

def check_Oxygen():
    """Helper function to instantly check if player has suffocated."""
    global Oxygen
    if Oxygen <= 0:
        print("\n==========================================")
        print("ALERT: Oxygen levels dropped to 0%!")
        print("You suffocated in the cold vacuum of space.")
        print("==========================================")
        restart_game()

def restart_game():
    """Resets all flags back to defaults and boots the player back to room 1."""
    global Oxygen, has_extinguisher, life_room_solved
    print("\n[SYSTEM] Initiating emergency revival protocols...")
    print("[SYSTEM] Resetting ship state values...\n")
    Oxygen = 100
    has_extinguisher = False
    life_room_solved = False
    medical_room()

def medical_room():
    global Oxygen # Added so you can heal and modify Oxygen
    
    print("\n------------MEDICAL ROOM------------")
    print("You see a first aid kit.")

    choice = input("Type 'first aid' to use it: ").strip().lower()
    if choice == "first aid":
        print("You use the first aid kit and heal yourself.")
        Oxygen += 20
        print("Your Oxygen level is now:", Oxygen)
        
    print("\nYou wake up in a life-support pod. Warning sirens are blaring.")
    print("The terminal shows current pressure is at 10 PSI.")
    print("To escape the pod, you must calibrate pressure to EXACTLY 50 PSI.")

    pressure = 10 # Initialized the variable properly
    
    while pressure != 50: # Fixed the uppercase P bug
        check_Oxygen()
        print(f"\n[STATUS] Pressure: {pressure} PSI | Oxygen: {Oxygen}%")
        choice = input("Enter command ('increase' to add 10 PSI / 'decrease' to drop 10 PSI): ").strip().lower()
        
        if choice == "increase":
            pressure += 10
            Oxygen -= 5
            print("You increase the pressure by 10 PSI.")
            print("Current Pressure:", pressure, "PSI")
            
            print("Oxygen level decreased by 5% due to exertion.")
            print("Current Oxygen:", Oxygen, "%")
        elif choice == "decrease":
            pressure -= 10
            Oxygen -= 5
            print("You decrease the pressure by 10 PSI.")
            print("Current Pressure:", pressure, "PSI")
            print("Oxygen level decreased by 5% due to exertion.")
            print("Current Oxygen:", Oxygen, "%")
        else:
            print("Invalid command. Please type 'increase' or 'decrease'.")

    print("\n[SUCCESS] Pressure stabilized at 50 PSI! The pod doors hiss open.")
    main_room()

def main_room():
    global Oxygen, has_extinguisher
    check_Oxygen()
    
    print("\n--- REGION 2: MAIN CONTROL HALL ---")
    print(f"[STATUS] Current Oxygen: {Oxygen}%")
    print("You step into the main control hall. The air is thick with smoke and the fire alarm is blaring.")
    print("Options:")
    print("1. 'life'   -> Enter Life Support Room and get Oxygen Suit")
    print("2. 'science'-> Enter Science Lab Room and get Fire Extinguisher")
    print("3. 'fire'   -> Try to clear the fire blocking the Control Room door")
    
    choice = input("What do you do? ").strip().lower()
    
    if choice == "life":
        if Oxygen >= 100:
            print("\n[DENIED] Your Oxygen tank is already completely full.")
            print("You have no reason to access Life Support. Go somewhere else!")
            main_room()
        else:
            life_room()
            
    elif choice == "science":
        if has_extinguisher == True:
            print("\n[DENIED] You already extracted the Fire Extinguisher from here.")
            print("The room is locked down. Go back to Life Room or Main Hall!")
            main_room()
        else:
            science_room()
            
    elif choice == "fire":
        if has_extinguisher == True and Oxygen >= 90:
            print("\n[SUCCESS] You squeeze the trigger of your extinguisher!")
            print("The freezing foam chokes out the electrical fire. The Bridge is exposed.")
            control_room()
        else:
            print("\n[BLOCKED] You cannot pass the fire.")
            print("You either do not possess a fire extinguisher, or your Oxygen")
            print("is below 90%, meaning you will pass out from the intense heat. Prepare first!")
            main_room() # Loop them back to selection instead of letting the script hang
    else:
        print("Invalid choice. Please choose 'life', 'science', or 'fire'.")
        main_room()

def life_room():
    global Oxygen, life_room_solved
    check_Oxygen()
    
    attempts = 3
    Code = "290" 
    
    print("\n--- REGION 3: LIFE SUPPORT ROOM ---")
    print(f"[STATUS] Current Oxygen: {Oxygen}%")
    print("The primary Oxygen reserve is locked behind a 3-digit system override code.")
    print("Security Alert: You have 3 lives (attempts) to crack the encryption.")
    print("Each failed attempt will trigger a shock and reduce your Oxygen by 10%.")
    print("\nHints:")
    print("The First Digit: Take the number of moons orbiting the planet Earth, then add the absolute number of primary planets closer to the Sun than Venus.")
    print("The Second Digit: Take the total number of primary planets in our solar system. Square that number. Add the digits and subtract the number of moons orbiting Mars.")
    print("The Third Digit: Count the total number of solid land surfaces you could physically step your feet onto if you traveled to Jupiter, Saturn, Uranus, and Neptune.")
    
    while attempts > 0:
        check_Oxygen()
        print(f"\n[ATTEMPTS REMAINING: {attempts}]")
        guess = input("Enter 3-digit override code: ").strip()
        
        if guess == Code:
            print("\n[CORRECT] Backup tanks engaged! Air rushing into your suit.")
            Oxygen = 200
            life_room_solved = True
            print("Oxygen boosted to 200%. Automatically returning to Main Control Hall.")
            main_room() 
            return 
        else:
            attempts -= 1
            Oxygen -= 10
            print(f"[WRONG CODE] Security system shocks you. Lost 10% Oxygen!")
            
    print("\n[FAIL] Security lockout activated. Room venting atmosphere completely!")
    restart_game()

def science_room():
    global Oxygen, has_extinguisher
    check_Oxygen()
        
    print("\n--- REGION 4: SCIENCE LAB ROOM ---")
    print(f"[STATUS] Current Oxygen: {Oxygen}%")
    print("The chemical safety cabinet contains the fire extinguisher, but it requires answering two terminal riddles.")
    
    print("\n------------------ RIDDLE 1 ------------------")
    print("[TERMINAL: RIDDLE 1 (Tricky)]")
    print("I leave the dark abyss to travel a vast distance across a vacuum, yet for millions of years, I age not a single day. I arrive at my destination to instantly die, and you can only see my past. What am I? \nhint: I am not a physical object, but a phenomenon.")
    
    attempts = 3
    while attempts > 0:
        check_Oxygen()
        print(f"[Riddle 1 Attempts Left: {attempts}]")
        ans1 = input("Your Answer: ").strip().lower()
        
        if ans1 == "photon":
            print("[ACCESS ACCORDED] First lock unlocked.")
            break
        else:
            attempts -= 1
            Oxygen -= 10
            print("[INCORRECT] Security defense active. Lost 10% Oxygen.")
            
    if attempts == 0:
        print("\n[FAIL] Failed Riddle 1. Lab safety gas deployed.")
        restart_game()
        return

    print("\n------------------ RIDDLE 2 ------------------")
    print("[TERMINAL: RIDDLE 2 (Normal)]")
    print("Which is the most shocking city in the world? \n(Hint: Its a city which you can't see but is in the dictionary.)")
    
    attempts = 3
    while attempts > 0:
        check_Oxygen()
        print(f"[Riddle 2 Attempts Left: {attempts}]")
        ans2 = input("Your Answer: ").strip().lower()
        
        if ans2 == "electricity":
            print("[ACCESS ACCORDED] Second lock unlocked.")
            break
        else:
            attempts -= 1
            Oxygen -= 10
            print("[INCORRECT] Security defense active. Lost 10% Oxygen.")
            
    if attempts == 0:
        print("\n[FAIL] Failed Riddle 2. Lab safety gas deployed.")
        restart_game()
        return

    has_extinguisher = True
    print("\n[SUCCESS] Vault doors unlatched. You grabbed the Fire Extinguisher!")
    print("Returning safely to Main Control Hall.")
    main_room()

def control_room():
    global Oxygen # Fixed casing from lowercase oxygen to Oxygen
    check_Oxygen()
    
    print("\n--- FINAL REGION: CORE CONTROL ROOM ---")
    print("The central mainframe AI is in front of you. To take back the ship, you must solve the Master Riddle.")
    print("Warning: You have exactly 5 attempts. Each failure costs 15% Oxygen.")
    
    print("\n[MASTER LOGIC PUZZLE]")
    print("A spaceship crew consists of a Captain, an Engineer, and a Pilot.")
    print("1. The Pilot only communicates on even-numbered calendar days.")
    print("2. The Engineer lies every single time the Captain speaks first.")
    print("3. Today is an odd-numbered calendar day, and the Captain has just spoken first.")
    print("Who is the only person guaranteed to tell the truth right now?")
    print("(Options to type: 'captain' / 'engineer' / 'pilot')")
    
    attempts = 5
    while attempts > 0:
        check_Oxygen()
        print(f"\n[FINAL LEVEL ATTEMPTS REMAINING: {attempts} | Oxygen: {Oxygen}%]")
        final_ans = input("Identify the truthful crew member: ").strip().lower()
        
        if final_ans == "captain":
            print("\n==========================================")
            print("CORRECT! The mainframe accepts your bypass logic.")
            print("The Captain is speaking first, so the rules don't force him to lie.")
            print("The AI drops its shields. You execute a hard reset.")
            print("YOU HAVE POWERED DOWN THE ROGUE SYSTEM AND WON THE GAME!")
            print("==========================================")
            sys.exit() 
        else:
            attempts -= 1
            Oxygen -= 50
            print("[ERROR] Wrong logical deduction! System feedback shocks your air grid! -50% Oxygen.")
            
    print("\n[CRITICAL FAILURE] Out of mainframe hack attempts.")
    restart_game()

# ==========================================
# RUN THE INITIAL SCRIPT CALL
# ==========================================
print("=== EMERGENCY PROTOCOL INITIALIZED ===")
medical_room()