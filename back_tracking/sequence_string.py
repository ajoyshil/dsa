"""
Given a keypad as shown in diagram, and an  𝑛
  digit number, list all words which are possible by pressing these numbers. The number that is input will only contain the digits 2 to 9; so, the only characters possible in your words are alphabetical characters.

For example, if the input number is  234
 , possible words which can be formed are (in alphabetical order):

adg adh adi aeg aeh aei afg afh afi bdg bdh bdi beg beh bei bfg bfh bfi cdg cdh cdi ceg ceh cei cfg cfh cfi
Format
Input - an  𝑛
 -digit number ( 0≤𝑛≤12
 ) (string); the number will be a string comprised of the digits 2 to 9

Output - list of words (list of strings); all the possible words that can be formed using the input (lower-cased)

"""


keypad_map = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

def get_possible_words(number):
    result = []
    def backtrack(combination, next_digits):
        if not next_digits:
            result.append(combination)
        else:
            for letter in keypad_map[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])
    backtrack("", number)
    return result

number = "23"
print(get_possible_words(number))