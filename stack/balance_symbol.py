def check_balance(input_string):
    # (){}[]]  {()}[]
    stack = []
    d = {"(": ")", "{": "}", "[": "]"}
    for c in input_string:

        if stack:

            if c == d[stack[-1]]:
                stack.pop()
            else:
                if c in d:
                    stack.append(c)
                else:
                    return "unbalance"

        else:
            if c not in d:
                return "unbalance"
            stack.append(c)
    return "balance"
#
# d = {"(": ")", "{": "}", "[": "]"}
#
# print("}"==d["{"])


str_lst = ["(){[]}", "[{()}]", "{[])", "}{[]", ]
for item in str_lst:
    print(check_balance(item))
