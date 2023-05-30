from utility import euler_totient_function, extended_gcd
from prime_generator import generate_prime
from dataclasses import dataclass


@dataclass
class PublicKey:
    n: int
    e: int


@dataclass
class PrivateKey:
    n: int
    d: int


def generate_key_pair(key_length: int = 2048, e: int = 65537):
    p, q = generate_prime(key_length // 2), generate_prime(key_length // 2)
    n = p * q
    phi_n = euler_totient_function(p, q)
    _, d, _ = extended_gcd(e, phi_n)
    
    public_key = PublicKey(n, e)
    private_key = PrivateKey(n, d)
    
    return public_key, private_key

