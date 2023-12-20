# Given a string str,
# reverse all words except the first and last words and print it
# Sample Input :  Hi how are you buddy
# Sample Output : Hi woh era uoy buddy

def reverse_sentence(sentence):
    words = sentence.split()
    # words = [word[::-1] for word in words[1:len(words)-1]]
    for i in range(len(words)):
        if i==0 or i ==len(words)-1:
            continue
        words[i] = words[i][::-1]
    return " ".join(words)


sentence = "Hi how are you buddy"
print(reverse_sentence(sentence))



def rev(s):
    s = list(s)
    l, r = 0, len(s)-1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return "".join(s)

print(rev("ABCD"))

def rev2(s):
    rev = ""
    for c in s:
        rev = c +  rev
    return rev

print(rev2("12345"))
