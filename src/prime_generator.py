from random import randrange, getrandbits


def is_prime(n: int, k: int = 128) -> int:
    """Tests if number is prime, using Miller-Rabin tests"""
    
    if n <= 1:
        return False
    if n <= 3:
        return True

    s = 0 #Generates number for Miller-Rabin tests
    r = n - 1
    while r % 2 == 0:
        s += 1
        r //= 2

    for _ in range(k): #Performs Miller-Rabin tests
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


def generate_possible_prime(bits: int = 1024) -> int:
    """Generates a number, which may possibly be prime"""
    
    n = getrandbits(bits)
    n |= (1 << bits - 1) | 1
    return n


def generate_prime(bits: int = 1024, k: int = 128) -> int:
    """Generates a number, which is most likely prime"""
    
    while not is_prime(n := generate_possible_prime(bits), k):
        pass
    return n
    
