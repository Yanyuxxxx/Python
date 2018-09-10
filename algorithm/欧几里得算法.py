
def gcd(m, n):

    while(n):
        rem = m % n
        m = n
        n = rem
    return m


print(gcd(7600, 2242))
print(gcd(2242, 7600))