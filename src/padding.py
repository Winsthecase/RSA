import random


def pad(text_bytes: bytes, padded_length: int) -> bytes:
    padding_length = padded_length - len(text_bytes) - 3
    padding_bytes = bytes([random.randint(1, 255) for _ in range(padding_length)])
    padded_text_bytes = b"\x00\x02" + padding_bytes + b"\x00" + text_bytes
    return padded_text_bytes


def unpad(padded_text_bytes: bytes) -> bytes:
    padding_start = padded_text_bytes.find(b"\x00", 2)
    text_bytes = padded_text_bytes[padding_start + 1:]
    return text_bytes
