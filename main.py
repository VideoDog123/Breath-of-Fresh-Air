#Jackson Rodosta
#Started: 3/5/2026
#Last updated: 3/13/2026
#BFA text adventure game. Takes user input to describe surroundings and move between rooms. The goal is to reach the surface.
#This is the main file that calls the necessary functions in order

from functions import act1, act2

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'
# color definitions for quick reference

def main():
# displays the title and starts act1, then act2, act3 is handled by room2_cave
    print(f"{BLUE}Welcome to Breath of Fresh Air")
    print(f"Use 1, 2, 3, and 4 to choose options when prompted\n")
    act1()
    act2()

if __name__ == '__main__':
    main()
