

def longest_sub_string(s):
    counter = {}
    l = max_str_len = 0
    for r in range(len(s)):
        cell_count = r - l + 1
        if not s[r] in counter:
            max_str_len = max(max_str_len, cell_count)
        else:
            if counter[s[r]] < l:
                max_str_len = max(max_str_len, cell_count)
            else:
                l = counter[s[r]] + 1
        counter[s[r]] = r
    return max_str_len

print(longest_sub_string("abcabcd"))