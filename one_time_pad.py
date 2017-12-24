import binascii
import random

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return int(bits.zfill(8 * ((len(bits) + 7) // 8)))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def encrypt(message, pad):
    binary_message = text_to_bits(message)
    return binary_message ^ pad

def decrypt(encrypted_message, pad):
    message = str(encrypted_message ^ pad)
    return text_from_bits(message)

def create_pad_of_equal_size(message):
    length = len(str(text_to_bits(message))) * 2
    pad = ''.join(map(str,[random.getrandbits(1) for i in range(length)]))
    return int(pad)

if __name__ == '__main__':
    message = "hola, world!"
    pad = create_pad_of_equal_size(message)

    encrypted_message = encrypt(message, pad)
    decrypted_message = decrypt(encrypted_message, pad)
    print(message)
    print(encrypted_message)
    print(decrypted_message)
