import base64

encoded_string = "JR4YFw8YLwA7Jx0mCRsaGBsMKhwSLwMdLhsBMC0YHBgwMwcBMBcmFBsfIjAHKxMVHBEBIAoXfA8="
decoded_bytes = base64.b64decode(encoded_string)

def xor_decrypt(ciphertext, key):
    return ''.join(chr(c ^ key[i % len(key)]) for i, c in enumerate(ciphertext))

# Brute-force the key
def brute_force_xor(decoded_bytes):
    possible_flags = []
    for key_length in range(1, 20):  # Brute force key length
        for possible_key in range(256):  # Guess plaintext
            key = [possible_key] * key_length
            decrypted = xor_decrypt(decoded_bytes, key)
            if "flag" in decrypted.lower():
                print(f"Key: {key}, Decrypted: {decrypted}")
                possible_flags.append(decrypted)
    return possible_flags

# Attempt to decrypt using brute force
result = brute_force_xor(decoded_bytes)

if result:
    print(f"\nPossible flags found ({len(result)} results):")
    for res in result:
        print(res)
else:
    print("No flag found")
