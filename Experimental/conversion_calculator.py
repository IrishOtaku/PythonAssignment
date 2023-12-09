# File: conversion_calculator.py


class ConversionCalculator:
    # A method to perform calculate unit conversions between different units
    def convert(self, conversion_type, value):
        # Calls the perform_conversion method and returns the result
        result = self.perform_conversion(conversion_type, value)
        return result

# Method for processing and delegating unit conversions
    def perform_conversion(self, conversion_type, value):
        # Split the conversion_type string into two units
        units = conversion_type.replace(' ', '_').lower().split('_to_')
        # Check if exactly two units are obtained
        if len(units) == 2:
            from_unit, to_unit = units
            # Delegates the actual conversion to the _convert method
            result = self._convert(from_unit, to_unit, value)
        else:
            # Return an error message for an invalid conversion type
            result = f"Invalid conversion type: {conversion_type}"
        return result
    # Method for actual unit conversion
    def _convert(self, from_unit, to_unit, value):
        # A dictionary containing the conversion facto
        conversion_factors = {
        # Conversion factors for various units all are self explanatory if you read the code itself

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
            # If a callable function is associated with the conversion, it uses it 
            if callable(conversion_factors[conversion_key]):
                # Use a lambda function for specific conversions
                result = conversion_factors[conversion_key](value)
            # If a simple conversion factor is associated, it will multiply the value by it.
            else:
                result = value * conversion_factors[conversion_key]
            return result
        else:
            # Returns an error message if the conversion is not supported
            return f"Conversion not supported: {from_unit} to {to_unit}"
