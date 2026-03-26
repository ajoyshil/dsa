# 🔹 Question

# Given a string s, find the length of the longest 
# substring without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: "abc" is the longest substring


# Input: s = "bbbbb"
# Output: 1
# Explanation: "b"

# Input: s = "pwwkew"
# Output: 3
# Explanation: "wke"

    

s = "abcabcbb"
s = "pwwkew"
s = "bbbdbb"
s = "abcabcdbb"


def longest_substring(s):
    d = {}
    start = 0
    max_length = 0

    for i in range(len(s)):
        if s[i] in d and d[s[i]] >= start:
            start = d[s[i]] + 1
        
        d[s[i]] = i
        max_length = max(max_length, i - start + 1)

    return max_length

res = longest_substring(s)      
print(res)