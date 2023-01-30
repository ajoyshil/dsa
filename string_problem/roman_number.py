rl = ["MCMIV", "VIII", "IX", "LXXI"]
def roman_to_int(roman_string):
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    roman_string = roman_string.replace("IV", "IIII").replace("IX", "VIIII")
    roman_string = roman_string.replace("XL", "XXXX").replace("XC", "LXXXX")
    roman_string = roman_string.replace("CD", "CCCC").replace("CM", "DCCCC")

    for c in roman_string:
        number += roman_dict[c]
    return number

roman_to_int("MCMIV")

def roman_to_int2(s):
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number= 0
    i = 0
    n = len(s)
    while i < n:
        temp = roman_dict[s[i]]
        if i != n-1 and temp < roman_dict[s[i+1]]:
            number = number + roman_dict[s[i+1]] - temp
            i +=2
        else:
            number = number + temp
            i += 1
    return number

for c in rl:
    print(roman_to_int(c))
    print(roman_to_int2(c))
