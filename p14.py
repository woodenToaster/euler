def even(n):
    return n // 2


def odd(n):
    return 3 * n + 1


def collatz(n):
    sequence = [n]
    while n > 1:
        sequence.append(even(n) if n % 2 == 0 else odd(n))
        n = sequence[-1]
    return sequence

if __name__ == '__main__':
    sequences = {i: len(collatz(i)) for i in range(1000000)}
    vals = list(sequences.values())
    index = vals.index(max(vals))
    print(list(sequences.keys())[index])
