def is_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

for c in range(1, 1000):
    for b in range(1, c):
        for a in range(1, b):
            if is_triplet(a, b, c) and a + b + c == 1000:
                print(a * b * c)
