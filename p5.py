import sys

for i in range(2520, 1000000000):
    for j in range(1, 21):
        if i % j != 0:
            break
    else:
        print(i)
        sys.exit(0)
