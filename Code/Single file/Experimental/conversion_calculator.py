# File: conversion_calculator.py


class ConversionCalculator:
    def convert(self, conversion_type, value):
        result = self.perform_conversion(conversion_type, value)
        return result

    def perform_conversion(self, conversion_type, value):
        units = conversion_type.replace(' ', '_').lower().split('_to_')
        if len(units) == 2:
            from_unit, to_unit = units
            result = self._convert(from_unit, to_unit, value)
        else:
            result = f"Invalid conversion type: {conversion_type}"
        return result

    def _convert(self, from_unit, to_unit, value):
        # Conversion factors for various units
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
            # Add more conversion factors as needed
        }

        conversion_key = (from_unit, to_unit)
        if conversion_key in conversion_factors:
            if callable(conversion_factors[conversion_key]):
                # Use a lambda function for specific conversions
                result = conversion_factors[conversion_key](value)
            else:
                result = value * conversion_factors[conversion_key]
            return result
        else:
            return f"Conversion not supported: {from_unit} to {to_unit}"
