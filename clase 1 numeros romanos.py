import unittest



def convert_decimal_to_roman(num):
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    miles = m[num // 1000]
    cientos = c[(num % 1000) // 100]
    decenas = x[(num % 100) // 10]
    unos = i[num % 10] 
    resultado = (miles + cientos + decenas + unos)
    return resultado



def roman_to_int(s):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(s)):
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
        else:
            int_val += rom_val[s[i]]
    return int_val
 


def suma(a, b):
    c = a + b
    return convert_decimal_to_roman(c)



class Testdecimaltoroman(unittest.TestCase):
    def test(self):
        for i in range(1, 4000):
            rom = convert_decimal_to_roman(i)
            num = roman_to_int(rom)
            self.assertEqual(i, num)



if __name__ == "__main__":
    unittest.main()

