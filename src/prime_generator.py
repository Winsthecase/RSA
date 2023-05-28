from random import randrange, getrandbits


def is_prime(n: int, k: int = 128):
    if n <= 1:
        return False
    if n <= 3:
        return True

    s = 0
    r = n - 1
    while r % 2 = 0:
        s += 1
        r //= 2

    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if == n - 1:
                break
        else:
            return False

    return True