#Roman number to Integer conversion
class roman_to_integer:
    def roman_to_int(self, s):
        roman_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integer_value = 0

        for i in range(len(s)):
            if i > 0 and roman_value[s[i]] > roman_value[s[i - 1]]:
                integer_value = integer_value + roman_value[s[i]] - 2 * roman_value[s[i - 1]]
            else:
                integer_value = integer_value + roman_value[s[i]]
        return integer_value

n = input('Enter roman number: ')

print('Integer value of ',n,' is ',roman_to_integer().roman_to_int(n))