# Captain's Mission Tracker - A manual Python project 
# Purpose: Practice core logic, loops, and conditional statements

def start_tracker():
    print("--- Welcome to the Captain's Mission Console ---")
    captain_name = input("Enter your name, Captain: ")
    missions_completed = 0
    
    while True:
        print(f"\nCommand Center: Welcome, Captain {captain_name}")
        print("1. Log New Mission")
        print("2. Check Rank")
        print("3. Exit Console")
        
        choice = input("Select an option (1-3): ")
        
        if choice == '1':
            mission_name = input("Enter Mission Name: ")
            difficulty = int(input("Enter Mission Difficulty (1-10): "))
            
            if difficulty > 7:
                print(f"Danger! {mission_name} is a high-risk mission.")
            else:
                print(f"Mission {mission_name} logged successfully.")
            
            missions_completed += 1
            
        elif choice == '2':
            if missions_completed == 0:
                print("Rank: Cadet (Complete a mission to promote)")
            elif missions_completed < 3:
                print("Rank: Pilot")
            else:
                print("Rank: Commander")
            print(f"Total Missions: {missions_completed}")
            
        elif choice == '3':
            print("Shutting down console... Safe travels, Captain!")
            break
        else:
            print("Invalid input. Please recalibrate.")

if __name__ == "__main__":
    start_tracker()
