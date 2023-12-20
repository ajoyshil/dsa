

import collections
def char_replacement(s, k):
    l = maxf = longest_str_len = 0
    count = {}
    for r in range(len(s)):
        if not s[r] in count:
            count[s[r]] = 0
        count[s[r]] += 1
        maxf = max(maxf, count[s[r]])
        cell_count = r - l + 1
        if cell_count - maxf <= k:
            longest_str_len = max(longest_str_len, cell_count)
        else:
            count[s[l]] -= 1
            if not count[s[l]]:
                count.pop(s[l])
            l += 1
    return longest_str_len

print(char_replacement("ABAB", 3))
