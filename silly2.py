import timeit


def test():
    for x in range(1000000):
        k = x + 1 + 2

print(timeit.timeit(test,number=1))