import base64
import itertools
import string


encoded_message = "IConIT0xdSoldit1GTJ2GTIudRkxdigidTQgMyoZMXY0KiIZdiAZJTQ/NjJ2Zzs="


decoded_bytes = base64.b64decode(encoded_message)


def xor_with_key(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])


def is_printable(data):
    try:
        return all(chr(b) in string.printable for b in data)
    except:
        return False


max_key_length = 4
possible_flags = []


for key_length in range(1, max_key_length + 1):
    for key in itertools.product(range(256), repeat=key_length):
        decoded_attempt = xor_with_key(decoded_bytes, key)
        if is_printable(decoded_attempt) and b'flag' in decoded_attempt.lower():
            possible_flags.append((decoded_attempt.decode('utf-8'), key))


for flag, key in possible_flags:
    print(f"Potential flag: {flag} | Key: {key}")
