import unittest
from math import gcd

# Zadanie 5.2

"""Skracanie ułamków"""
def skracanie(ułamek):

    licznik, mianownik = ułamek

    if mianownik < 0:
        licznik, mianownik = -licznik, - mianownik
    
    g = gcd(licznik, mianownik)
    return [licznik // g, mianownik // g]

"""Sumowanie ułamków"""
def dodawanie(ułamek1, ułamek2):
    a, b = ułamek1
    c, d = ułamek2

    return skracanie([a * d + b * c, b * d])

"""Odejmowanie ułamków"""
def odejmowanie(ułamek1, ułamek2):
    a, b = ułamek1
    c, d = ułamek2

    return skracanie([a * d - b * c, b * d])

"""Mnożenie"""
def mnożenie(ułamek1, ułamek2):
    a, b = ułamek1
    c, d = ułamek2

    return skracanie([a * c, b * d])

"""Dzielenie"""
def dzielenie(ułamek1, ułamek2):
    a, b = ułamek1
    c, d = ułamek2

    return skracanie([a * d, b * c])

"""Sprawdzenie znaku"""

def znak(ułamek):
    return ułamek[0] * ułamek[1] > 0

"""Sprawdzanie zera"""
def zero(ułamek):
    return ułamek[0] == 0

"""Porównywanie"""
def porównaj(ułamek1, ułamek2):
    a, b = ułamek1
    c, d = ułamek2
    if a * d < b * c:
        return -1
    elif a * d > b * c:
        return 1
    else:
        return 0

"""Konwersja do float"""
def konwersja(ułamek):
    return ułamek[0] / ułamek[1]

class TestFractions(unittest.TestCase):
    def test_dodawanie(self):
        self.assertEqual(dodawanie([1, 2], [1,3]), [5,6])

    def test_odejmowanie(self):
        self.assertEqual(odejmowanie([3, 4], [1, 2]), [1, 4])

    def test_mnożenie(self):
        self.assertEqual(mnożenie([2, 3], [3, 4]), [1, 2])
    
    def test_dzielenie(self):
        self.assertEqual(dzielenie([1, 2], [3, 4]), [2, 3])
    
    def test_znak(self):
        self.assertTrue(znak([4, 5]))
        self.assertFalse(znak([-1, 8]))
    
    def test_zero(self):
        self.assertTrue(zero([0,3]))
        self.assertFalse(zero([8, 9]))

    def test_porównaj(self):
        self.assertEqual(porównaj([1, 2], [2, 4]), 0)
        self.assertEqual(porównaj([1, 3], [1, 2]), -1)
        self.assertEqual(porównaj([3, 2], [1, 2]), 1)

    def test_konwersja(self):
        self.assertAlmostEqual(konwersja([1,2]), 0.5)

if __name__ == '__main__':
    unittest.main()
# Wyniki testu w terminalu:
# PS C:\Users\User> & C:/Users/User/AppData/Local/Microsoft/WindowsApps/python3.13.exe "c:/Users/User/Desktop/uj/sem I/Python/main.py/Lekcja 5/fracs.py"
# ........
# ----------------------------------------------------------------------
# Ran 8 tests in 0.001s

# OK
# PS C:\Users\User> 
