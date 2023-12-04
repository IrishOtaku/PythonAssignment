from conversion_calculator import ConversionCalculator
from menu_functions import main_menu, distance_menu, temperature_menu, volume_menu, mass_menu, area_menu

if __name__ == "__main__":
    calc = ConversionCalculator()
    while True:
        choice = main_menu()
        if choice == 6:
            break
        elif choice == 1:
            distance_menu(calc)
        elif choice == 2:
            temperature_menu(calc)
        elif choice == 3:
            volume_menu(calc)
        elif choice == 4:
            mass_menu(calc)
        elif choice == 5:
            area_menu(calc)