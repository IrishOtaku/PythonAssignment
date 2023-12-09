# File: menus.py

# Import the pytest library for testing
import pytest

# Import the ConversionCalculator class from the conversion_calculator module within the same directory
from conversion_calculator import ConversionCalculator

# Define the main_menu function in same directory with code for displaying conversion options and getting user input
def main_menu():
    print("\nSelect a conversion option:")
    print("1. Acres To Hectares (ha)")
    print("2. Celsius To Fahrenheit (°F)")
    print("3. Fahrenheit To Celsius (°C)")
    print("4. Hectares To Acres (acres)")
    print("5. Kilogram To Stones (stones)")
    print("6. Kilometres To Miles (miles)")
    print("7. Litres To Pints (pints)")
    print("8. Miles To Kilometres (km)")
    print("9. Pints To Litres (litres)")
    print("10. Stones To Kilogram (kg)")
    print("11. Quit")

    # Clear input buffer to avoid unexpected input and fixes bugs with keyboard input
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys
        sys.stdin.flush()

    # Get user input for the chosen conversion option
    choice = int(input("Choose an option: "))
    return choice

# Define the perform_conversion function for executing the chosen conversion
def perform_conversion(choice, calc):
    if choice == 11:
        # Quit the program if option 11 is chosen
        print("Exiting the program.")
        exit()
    elif choice == 6:
        # Option 6 is Kilometres To Miles, get user input and perform the conversion
        value = float(input("Enter the distance in kilometers: "))
        result = calc.convert("kilometres_to_miles", value)
        print(f"Result: {result} miles")
    else:
        # For other options, get the conversion type, user input, and perform the conversion
        conversion_type = get_conversion_type(choice)
        if conversion_type:
            value = float(input(f"Enter the value to convert from {conversion_type}: "))
            unit_symbol = get_unit_symbol(conversion_type)
            result = calc.convert(
                conversion_type.replace(' ', '_').lower(),
                value
            )
            print(f"Result: {result} {unit_symbol}")
        else:
            print("Invalid conversion type. Please try again.")

# Define the get_conversion_type function to retrieve the conversion type based on user choice
def get_conversion_type(choice):
    conversion_options = [
        "Acres To Hectares", "Celsius To Fahrenheit", "Fahrenheit To Celsius",
        "Hectares To Acres", "Kilogram To Stones", "Kilometres To Miles",
        "Litres To Pints", "Miles To Kilometres", "Pints To Litres",
        "Stones To Kilogram"
    ]
    return conversion_options[choice - 1] if 1 <= choice <= 10 else None

# Define the get_unit_symbol function to retrieve the unit symbol based on the conversion type
def get_unit_symbol(conversion_type):
    symbols = {
        "Acres To Hectares": "ha",
        "Celsius To Fahrenheit": "°F",
        "Fahrenheit To Celsius": "°C",
        "Hectares To Acres": "acres",
        "Kilogram To Stones": "stones",
        "Kilometres To Miles": "miles",
        "Litres To Pints": "pints",
        "Miles To Kilometres": "km",
        "Pints To Litres": "litres",
        "Stones To Kilogram": "kg",
    }
    return symbols.get(conversion_type, "")
