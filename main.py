# ================================================================
# Program: Mine Runner Game
# Author: Logan Smith
# Description: A fun game where you avoid the mines as you avoid a chaser.
# Date Modified: 05/15/2024
# Version: 2.0


# Import Libraries
# ================================================================
from classes import *

# Future Functionality
# ================================================================
# Fix overlapping mines and obstacles X
# Adjust the static values to be dynamic
# Add a pause screen
# Add A game opening screen
# Clean up the main loop
# Add images to game
# Add powerups (see mines around you)

def main():
    """Main function that runs the program."""
    mine_runner = Game()
    menu = Menu()
    menu = menu.display_menu()
    mine_runner.play()
    
    return 0


if __name__ == "__main__":
    main()

