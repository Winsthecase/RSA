from utility import euler_totient_function, extended_gcd
from prime_generator import generate_prime
from padding import pad, unpad
from dataclasses import dataclass
from typing import Tuple
import sys


PADDING_LENGTH = 11


@dataclass
class PublicKey:
    n: int
    e: int
    key_length: int

    def encrypt(self, text: str, padding_length: int = 11) -> bytes:
        block_length = self.key_length // 8 - padding_length
        text_bytes = text.encode()

        ciphertext = b""
        for block_start in range(0, len(text_bytes), block_length):
            text_block = text_bytes[block_start: block_start + block_length]
            padded_block = pad(text_block, self.key_length // 8)
            numerical_block = int.from_bytes(padded_block, "big")

            ciphertext_block = pow(numerical_block, self.e, self.n).to_bytes(self.key_length // 8, "big")
            ciphertext += ciphertext_block
        
        return ciphertext


@dataclass
class PrivateKey:
    n: int
    d: int
    key_length: int

    def decrypt(self, ciphertext: bytes) -> str:
        block_length = self.key_length // 8
        
        text_bytes = b""
        for block_start in range(0, len(ciphertext), block_length):
            ciphertext_block = ciphertext[block_start: block_start + block_length]
            numerical_block = int.from_bytes(ciphertext_block, "big")

            text_block = pow(numerical_block, self.d, self.n).to_bytes(self.key_length // 8, "big")
            unpadded_block = unpad(text_block)
            text_bytes += unpadded_block

        text = text_bytes.decode()
        
        return text


def generate_key_pair(key_length: int = 2048, e: int = 65537) -> Tuple[PublicKey, PrivateKey]:
    p, q = generate_prime(key_length // 2), generate_prime(key_length // 2)
    n = p * q
    phi_n = euler_totient_function(p, q)
    _, d, _ = extended_gcd(e, phi_n)
    
    public_key = PublicKey(n, e, key_length)
    private_key = PrivateKey(n, d, key_length)
    
    return public_key, private_key


if __name__ == "__main__":
    public_key, private_key = generate_key_pair(1024)
    encrypted_data = public_key.encrypt("This is some testing text.")
    decrypted_data = private_key.decrypt(encrypted_data)
