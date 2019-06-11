
import string
import random
import string_sum

def unique_count(val):
    ls = set(list(val))
    return len(ls)

val = ''.join(random.choice(string.printable) for i in range(1000000))

def test_pure_python(benchmark):
    benchmark(unique_count, val)

def test_mod_rust(benchmark):
    benchmark(string_sum.unique_count, val)
