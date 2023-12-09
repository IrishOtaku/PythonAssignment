# File: combined_converter.py

# Define the ConversionCalculator class for handling unit conversions
class ConversionCalculator:

    # Method to perform unit conversions
    def convert(self, conversion_type, value):
        # Calls the perform_conversion method and returns the result
        result = self.perform_conversion(conversion_type, value)
        return result

    # Method for processing and delegating unit conversions
    def perform_conversion(self, conversion_type, value):
        # Split the conversion_type string into two units
        units = conversion_type.replace(' ', '_').lower().split('_to_')
        
        # A Check if exactly two units are obtained
        if len(units) == 2:
            from_unit, to_unit = units
            # Delegates the actual conversion to the _convert method
            result = self._convert(from_unit, to_unit, value)
        else:
            # Returns an error message for an invalid conversion type
            result = f"Invalid conversion type: {conversion_type}"
        return result

    # Method for actual unit conversions the ones that are integrated into the program
    def _convert(self, from_unit, to_unit, value):
        # A dictionary containing the conversion factors and functions
        conversion_factors = {
            ('acres', 'hectares'): 0.404686,
            ('celsius', 'fahrenheit'): lambda x: (x * 9/5) + 32,
            ('fahrenheit', 'celsius'): lambda x: (x - 32) * 5/9,
            ('hectares', 'acres'): 2.47105,
            ('kilogram', 'stones'): 0.157473,
            ('kilometres', 'miles'): 0.621371,
            ('litres', 'pints'): 1.75975,
            ('miles', 'kilometres'): 1.60934,
            ('pints', 'litres'): 0.568261,
            ('stones', 'kilogram'): 6.35029,
        }

        # Creates a tuple representing the pair of units
        conversion_key = (from_unit, to_unit)
        
        # Check if the conversion is supported
        if conversion_key in conversion_factors:
            # If a callable function is associated with the conversion, use it 
            if callable(conversion_factors[conversion_key]):
                # Use a lambda function for specific conversions
                result = conversion_factors[conversion_key](value)
            # If a simple conversion factor is associated, multiply the value by it
            else:
                result = value * conversion_factors[conversion_key]
            return result
        else:
            # Returns an error message if the conversion is not supported
            return f"Conversion not supported: {from_unit} to {to_unit}"

# Function to display the main menu and get user input
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

# Function to perform the chosen conversion
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

# Function to retrieve the conversion type based on user choice
def get_conversion_type(choice):
    conversion_options = [
        "Acres To Hectares", "Celsius To Fahrenheit", "Fahrenheit To Celsius",
        "Hectares To Acres", "Kilogram To Stones", "Kilometres To Miles",
        "Litres To Pints", "Miles To Kilometres", "Pints To Litres",
        "Stones To Kilogram"
    ]
    return conversion_options[choice - 1] if 1 <= choice <= 10 else None

# Function to retrieve the unit symbol based on the conversion type
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

# Main function to run the program
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
