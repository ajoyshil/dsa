from collections import defaultdict


def group_anagram(strs):
    anagram_map = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    return list(anagram_map.values())


strs = ["eat","tea","tan","ate","nat","bat"]

print(group_anagram(strs))

def sum(a, b):
    print(a+-b)

sum(2,3)