import random
import statistics

def fisher_yates(l):
    out_list = []
    while l:
        out_list.append(l.pop(random.randint(0, len(l)-1)))
    return out_list

def fisher_yates(l):
    for i in range(len(l)-1):
        j = random.randint(i, len(l)-1)
        l[j], l[i] = l[i], l[j]
    return l


def is_anagram(lhs, rhs):
    return sorted(lhs) == sorted(rhs)

def is_prime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def test():
    assert is_anagram("race", "care")
    assert is_anagram("Race", "caRe")
    assert not is_anagram("racer", "care")
    assert not is_anagram("race", "carer")
    assert is_anagram("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba")
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert not is_prime(1)
    assert not is_prime(25)
    assert not is_prime(4)
    assert not is_prime(6)
    assert not is_prime(9)
    test_fisher_yates()

def test_fisher_yates():
    shuffled_lists = []
    for i in range(10000):
        shuffled_lists.append(fisher_yates(list(range(100))))
    positional_sums = [sum(l) for l in zip(*shuffled_lists)]
    tot = sum(positional_sums)
    stddev = statistics.stdev(positional_sums)
    print(stddev, tot, stddev/(tot/100))


if __name__ == "__main__":
    test()
