# File: menus.py

import pytest
from conversion_calculator import ConversionCalculator

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

    # Clear input buffer
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys
        sys.stdin.flush()

    choice = int(input("Choose an option: "))
    return choice

def perform_conversion(choice, calc):
    if choice == 11:
        print("Exiting the program.")
        exit()
    elif choice == 6:
        # Option 6 is Kilometres To Miles
        value = float(input("Enter the distance in kilometers: "))
        result = calc.convert("kilometres_to_miles", value)
        print(f"Result: {result} miles")
    else:
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

def get_conversion_type(choice):
    conversion_options = [
        "Acres To Hectares", "Celsius To Fahrenheit", "Fahrenheit To Celsius",
        "Hectares To Acres", "Kilogram To Stones", "Kilometres To Miles",
        "Litres To Pints", "Miles To Kilometres", "Pints To Litres",
        "Stones To Kilogram"
    ]
    return conversion_options[choice - 1] if 1 <= choice <= 10 else None

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
