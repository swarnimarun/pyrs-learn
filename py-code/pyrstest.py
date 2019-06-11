
import string
import random

def unique_count(val):
    ls = []
    for x in val:
        if not x in ls:
            ls.append(x)
    print(len(ls))

val = ''.join(random.choice(string.printable) for i in range(1000000))

def test_pure_python(benchmark):
    benchmark(unique_count, val)
