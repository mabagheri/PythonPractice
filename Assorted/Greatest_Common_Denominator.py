def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        a = b
        b = r
        return gcd(a, b)


print(gcd(205, 11))