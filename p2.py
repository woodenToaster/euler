computed_vals = {}


def fib(x):
    if x == 1:
        return x
    if x == 2:
        return x
    if x in computed_vals:
        return computed_vals[x]
    else:
        val = fib(x - 1) + fib(x - 2)
        computed_vals[x] = val
        return val

l = []

for i in range(1, 1000):
    f = fib(i)
    if f > 4000000:
        break
    if f % 2 == 0:
        l.append(f)

print(sum(l))
