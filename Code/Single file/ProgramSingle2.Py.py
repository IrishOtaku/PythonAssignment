# File1: main_program.py

from conversion_calculator import ConversionCalculator


def main_menu():
    print("1. Acres To Hectares")
    print("2. Celsius To Fahrenheit")
    print("3. Fahrenheit To Celsius")
    print("4. Hectares To Acres")
    print("5. Kilogram To Stones")
    print("6. Kilometres To Miles")
    print("7. Litres To Pints")
    print("8. Miles To Kilometres")
    print("9. Pints To Litres")
    print("10. Stones To Kilogram")
    print("q. Quit")
    choice = input("Choose an option: ")
    return choice


def perform_conversion(choice, calc):
    if choice == 'q':
        print("Exiting the program.")
        exit()

    value = float(input(f"Enter the value to convert: "))
    result = getattr(calc, choice.replace(' ', '_').lower())(value)
    print(f"Result: {result}")


def main():
    calc = ConversionCalculator()
    while True:
        choice = main_menu()
        if choice == 'q':
            break
        elif choice.isdigit() and 1 <= int(choice) <= 10:
            perform_conversion(choice, calc)
        else:
            print("Invalid choice. Please enter a number between 1 and 10, or 'q' to quit.")


if __name__ == "__main__":
    main()
