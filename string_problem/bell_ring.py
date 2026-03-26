


def ring(st):
    count = 0
    pattern_set = {'1100', '0011'}
    if len(st) < 4:
        return -1
    temp = st[:4]
    if st[:4] in pattern_set:
        count +=1


    i,k = 1,4
    while i< len(st)-k:
        temp = st[i:i + k]
        if st[i:i+k] in pattern_set:
            count +=1
            i = i+k-1
            continue
        i+=1
    # count = sum(st.count(x) for x in sset)
    print(count)
    # while '1100' in st or '0011' in st:
    #     if '1100' in st:
    #         count +=1
    #         st.replace('11')
    return count


input_str = ["101101101100001100101", "110011001100"]
for s in input_str:
    print(ring(s))
