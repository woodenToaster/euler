n1 = 999
n2 = 999


def is_palindrome(n):
    n_str = str(n)
    length = len(n_str)
    odd = length % 2
    first_half = n_str[:length // 2]
    second_half = n_str[length // 2 + odd:]
    for i, j in zip(first_half, reversed(second_half)):
        if i != j:
            return False
    return True

print(max(i * j
          for i in reversed(range(n1 + 1))
          for j in reversed(range(n2 + 1))
          if is_palindrome(i * j)))
