# File: main_program.py

from conversion_calculator import ConversionCalculator
from menus import main_menu, perform_conversion

def main():
    calc = ConversionCalculator()
    while True:
        choice = main_menu()
        if choice == 11:
            print("Exiting the program.")
            break
        elif 1 <= choice <= 10:
            perform_conversion(choice, calc)

if __name__ == "__main__":
    main()
