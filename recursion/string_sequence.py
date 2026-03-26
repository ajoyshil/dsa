def string_sequence(s):
    return generate_sequence(s, "", 0, [])


def generate_sequence(s, current, i, arr):
    # arr.append(current)
    if len(s) == i:
        arr.append(current)
        return
    generate_sequence(s, current + s[i], i+1, arr)
    generate_sequence(s, current, i+1, arr)
    return sorted(arr)


print(string_sequence("abc"))

