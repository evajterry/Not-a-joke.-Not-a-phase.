class Kerrigan:
    def __init__(self):
        self.name = "Kerrigan"
        self.number_of_feet = 2
        self.proximity_to_eva = 10
        self.foot_pick_up_lines = []

    def distance_calculator(self, user_response):
        if user_response == "2":
            self.proximity_to_eva += 1
        elif user_response == "3":
            self.proximity_to_eva -= 1
    
    def growing_feet(self, user_response):
        self.number_of_feet += 1

def does_kerrigan_send_feet_pics(kerrigan):
    if len(kerrigan.foot_pick_up_lines) > 0:
        toe_lines = []
        for pick_up_line in kerrigan.foot_pick_up_lines:
            if "toes" or "toe" in pick_up_line.lower().strip():
                toe_lines.append(pick_up_line)
                return toe_lines
            else:
                return "Kerrigan does not send feet pics, and you need better pickup lines."
    
    elif kerrigan.proximity_to_eva > 2: 
        return "Eva is so close to Kerrigan. Kerrigan sends more than one foot pic."

    elif kerrigan.proximity_to_eva < 5 or len(kerrigan.foot_pick_up_lines) > 0:
        return "Kerrigan sends feet pics"

    elif kerrigan.proximity_to_eva == 10 or kerrigan.number_of_feet > 2:
        return "Kerrigan will think about sending feet pics"

    else:
        return "Kerrigan does not send feet pics"
    
def main():
    kerrigan = Kerrigan()
    print("\nWelcome, family. If you would like to exit this program, simply enter an empty string. \nThe goal of this program is to have Kerrigan send as many foot pics as possible to Eva.")
    while True:
        print("\nHere are some options of things to do. \n 1. Say a foot pickup line. \n 2. Increase Eva's proximity to Kerrigan. \n 3. Get Kerrigan further away from Eva. \n 4. Increase Kerrigan's number of feet. \n 5. See how how close you are to getting a foot pic.")
        user_input = input("What would you like to do? \n")
        if user_input == "":
            print("See you later!")
            break
        elif user_input == "1":
            print("Please enter a foot pickup line.")
            foot_pickup_line = input()
            kerrigan.foot_pick_up_lines.append(foot_pickup_line)
        elif user_input == "2":
            print("Distance between Kerrigan and Eva decreasing.")
            kerrigan.distance_calculator(user_input)
        elif user_input == "3":
            print("Distance between Eva and Kerrigan increasing.")
            kerrigan.distance_calculator(user_input)
        elif user_input == "4":
            print("Kerrigan's number of feet increased.")
            kerrigan.growing_feet(user_input)
        elif user_input == "5":
            does_kerrigan_send_feet_pics(kerrigan)
            print(f"Kerrigan is {kerrigan.proximity_to_eva} feet away from Eva.")
            print(f"Kerrigan has {kerrigan.number_of_feet} feet.")
            print(f"Kerrigan has {len(kerrigan.foot_pick_up_lines)} foot pickup lines.")
            print(f"Kerrigan's foot pickup lines are: {kerrigan.foot_pick_up_lines}")
        else:
            print("Please enter a valid option.")

if __name__=="__main__":
    main()