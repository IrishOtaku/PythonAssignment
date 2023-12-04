from menu_functions import main_menu, distance_menu, temperature_menu, volume_menu, mass_menu, area_menu, convert_value
from conversion_calculator import ConversionCalculator
import pytest

def test_main_menu(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    assert main_menu() == 1

def test_distance_menu(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '2')
    assert distance_menu() == 2

def test_temperature_menu(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    assert temperature_menu() == 1

def test_volume_menu(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '2')
    assert volume_menu() == 2

def test_mass_menu(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    assert mass_menu() == 1

def test_area_menu(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '2')
    assert area_menu() == 2

def test_convert_value():
    calc = ConversionCalculator()
    assert convert_value(1, 1, 10, calc) == 16.0934
    assert convert_value(1, 2, 16.0934, calc) == 10
    assert convert_value(2, 1, 0, calc) == 32
    assert convert_value(2, 2, 32, calc) == 0
    assert convert_value(3, 1, 2, calc) == 0.946352
    assert convert_value(3, 2, 1, calc) == 2.11338
    assert convert_value(4, 1, 70, calc) == 11.0231
    assert convert_value(4, 2, 11.0231, calc) == 70
    assert convert_value(5, 1, 5, calc) == 2.02343
    assert convert_value(5, 2, 2.02343, calc) == 5

