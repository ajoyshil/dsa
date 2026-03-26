def set_bit(n,i):
    mask = 1 <<i
    n = mask | n
    print(bin(n))

# set_bit(8,2)

def clear_bit(n,i):
    print(bin(n))
    mask = 1<<i  # 1000
    print(bin(mask))
    mask = ~mask
    print(bin(mask))
    n = n&mask
    print(bin(n))

clear_bit(15,2)
