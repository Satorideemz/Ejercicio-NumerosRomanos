import unittest
from numerosromanos import convert_decimal_to_roman, roman_to_int,suma

class Testdecimaltoroman(unittest.TestCase):
    def test(self):
        for i in range(1, 4000):
            rom = convert_decimal_to_roman(i)
            num = roman_to_int(rom)
            self.assertEqual(i, num)



if __name__ == "__main__":
    unittest.main()