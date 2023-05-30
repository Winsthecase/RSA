def euler_totient_function(p: int, q: int) -> int:
    return (p - 1) * (q - 1)


def extended_gcd(a: int, b: int) ->  int:
    if b == 0:
        return a, 1, 0

    gcd, x_prev, y_prev = extended_gcd(b, a % b)
    x = y_prev
    y = x_prev - (a // b) * y_prev

    return gcd, x, y
