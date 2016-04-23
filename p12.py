from functools import reduce


def triangle_number():
    n = 0
    for i in range(1, 1000000):
        yield n + i
        n = n + i


def get_factors(n):
    return set(reduce(list.__add__,
               [[i, i // n]
                for i in range(1, int(n ** 0.5) + 1)
                if n % i == 0]))

if __name__ == '__main__':

    divisors = 0
    gen = triangle_number()

    while divisors < 502:
        tri_num = next(gen)
        divisors = len(get_factors(tri_num)) * 2
    print(tri_num)
