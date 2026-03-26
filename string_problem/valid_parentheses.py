"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

[{()}]
"""


def valid_parentheses(s):
    map = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    stack = []
    for c in s:
        if not stack:
            if c not in map:
                return False
            stack.append(c)
        else:
            if c not in map:
                if map[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
    return True if not stack else False

print(valid_parentheses("[{]()}]"))
