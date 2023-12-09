# Assignment of Python Skill Demonstration 3 - Joshua Gill

# Created by Joshua Gill, unfortunately I couldn't attend classes due to a lot going in my life, but attempted to do this with my Mom as she programs as well and I am well aware that this was a team based Assignment 




# Import the pytest library for testing
import pytest

# Import the ConversionCalculator class from the conversion_calculator module otherwise the module I created which is in the same directory it calls from her
from conversion_calculator import ConversionCalculator

# Import the main_menu and perform_conversion functions from the menus module contained in the same directory I programmed 
from menus import main_menu, perform_conversion

# Define the main function
def main():
    # Create an instance of the ConversionCalculator class
    calc = ConversionCalculator()

    # Start an infinite loop for the main program
    while True:
        # Call the main_menu function to display the options and get user input
        choice = main_menu()

        # Check if the user chose option 11 to exit the program
        if choice == 11:
            # Print a message and break out of the loop
            print("Exiting the program.")
            break
        # Check if the user chose an option between 1 and 10
        elif 1 <= choice <= 10:
            # Call the perform_conversion function with the chosen option and the calculator instance
            perform_conversion(choice, calc)

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Calls the main function
    main()
