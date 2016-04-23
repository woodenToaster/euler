n = 10001
primes = {}


def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            primes[x] = False
            return False
    primes[x] = True
    return True


def next_prime(n):
    for i in range(2, n):
        if is_prime(i):
            yield i

count = 1
for p in next_prime():
    if count == n:
        print(p)
        break
    count += 1
    print(count)
