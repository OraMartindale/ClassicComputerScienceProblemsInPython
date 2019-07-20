from secrets import token_bytes

def random_key(length):
    return int.from_bytes(token_bytes(length), "big")

def encrypt(original):
    original_bytes = original.encode()
    dummy = random_key(len(original_bytes))
    original_key = int.from_bytes(original_bytes, "big")
    encryped = original_key ^ dummy
    return dummy, encryped

def decrypt(key1, key2):
    decrypted = key1 ^ key2
    temp = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()

if __name__ == "__main__":
    key1, key2 = encrypt("One Time Pad!")
    result = decrypt(key1, key2)
    print(key1)
    print(key2)
    print(result)
