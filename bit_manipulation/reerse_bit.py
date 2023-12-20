class Reverse:
    def reverseBits(ajoy, n):
        out = 0
        for i in range(32):
            out = (out << 1) ^ (n & 1)
            n >>= 1
        return out


Reverse().reverseBits(11101000)