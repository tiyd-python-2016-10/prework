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


if __name__ == "__main__":
    test()
