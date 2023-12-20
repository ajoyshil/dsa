# checking the ith bit, wheather set or not

def check_bit(n, i):
    mask = 1<<i
    print(bin(mask))
    print(mask)
    if mask & n==0:
        print(0)
    else:
        print(1)


check_bit(4,2)

# check last bit set or not

def check_last_bit(n): # This is also way to check a number is even or odd
    if n&1==1:
        print("last bit of {}: is 1 and number is odd".format(n))
    else:
        print("last bit of {}: is 0 and number is even".format(n))


check_last_bit(99)
