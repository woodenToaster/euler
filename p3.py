num = 600851475143
primes = {}


def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            primes[x] = False
            return False
    primes[x] = True
    return True


def get_largest_prime_factor(x):
    largest = 0
    # Get largest factor
    for i in range(3, x // 2):
        if x % i == 0 and i % 2 != 0:
            # See if it's prime
            if primes.get(i, is_prime(i)):
                if i > largest:
                    largest = i
                    print(i)
    return largest

print(get_largest_prime_factor(num))
