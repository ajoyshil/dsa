input = "My name is Ajoy Shil"
output = "My NaMe Is AjOy ShIl"


def solv(s):
    new_string = ""
    i = 0
    for c in s:
        if c.isalnum():
            if i % 2 ==0:
                new_string += c.upper()
            else:
                new_string += c.lower()
            i +=1
        else:
            new_string += ' '
    return new_string

print(solv(input))
