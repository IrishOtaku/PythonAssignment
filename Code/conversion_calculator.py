class ConversionCalculator:
    def miles_to_kilometres(self, miles):
        return miles * 1.60934

    def kilometres_to_miles(self, kilometres):
        return kilometres / 1.60934

    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

    def pints_to_litres(self, pints):
        return pints * 0.473176

    def litres_to_pints(self, litres):
        return litres / 0.473176

    def kilogram_to_stones(self, kilogram):
        return kilogram * 0.157473

    def stones_to_kilogram(self, stones):
        return stones / 0.157473

    def acres_to_hectares(self, acres):
        return acres * 0.404686

    def hectares_to_acres(self, hectares):
        return hectares / 0.404686
