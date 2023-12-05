# File1: main_program.py

from conversion_calculator import ConversionCalculator
import pytest

def main_menu():
    print("1. Distance")
    print("2. Temperature")
    print("3. Volume")
    print("4. Mass")
    print("5. Area")
    print("6. Quit")
    choice = int(input("Choose an option: "))
    return choice

def generate_conversion_menu(options):
    print("Select a conversion option:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    return int(input("Choose an option: "))

def generate_conversion_options(calc):
    options = []
    for method_name in dir(calc):
        if not method_name.startswith("__") and callable(getattr(calc, method_name)):
            options.append(method_name.replace('_', ' ').title())
    return options

def perform_conversion(choice, calc):
    if choice == 6:
        print("Exiting the program.")
        return

    conversion_options = generate_conversion_options(calc)
    sub_choice = generate_conversion_menu(conversion_options)
    value = float(input(f"Enter the value to convert from {conversion_options[sub_choice - 1]}: "))
    result = getattr(calc, conversion_options[sub_choice - 1].replace(' ', '_').lower())(value)
    print(f"Result: {result}")

def distance_menu(calc):
    perform_conversion(1, calc)

def temperature_menu(calc):
    perform_conversion(2, calc)

def volume_menu(calc):
    perform_conversion(3, calc)

def mass_menu(calc):
    perform_conversion(4, calc)

def area_menu(calc):
    perform_conversion(5, calc)

def main():
    calc = ConversionCalculator()
    while True:
        choice = main_menu()
        if choice == 6:
            break
        elif 1 <= choice <= 5:
            perform_conversion(choice, calc)

if __name__ == "__main__":
    main()
