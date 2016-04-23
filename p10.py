n = 2000000
ints = {x: True for x in range(2, n)}
p = 2


def get_next_prime(n):
    for x in range(p + 1, n + 1):
        if ints[x] is True:
            return x
    return None

more_primes = True
while more_primes:
    for x in range(2 * p, n + 1, p):
        ints[x] = False
    p = get_next_prime(n)
    if p is None:
        print(sum(x for x in ints if ints[x] is True))
        more_primes = False
