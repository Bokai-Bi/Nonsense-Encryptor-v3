import random

def encrypt(fileName, seed_provided, newF):
    random.seed(seed_provided)
    with open(fileName, "rb") as readF:
        with open(newF, "wb") as writeF:
            byte_arr = bytearray(readF.read())
            writeF.write(encrypt_bytes(byte_arr, seed_provided))
            
def encrypt_bytes(byte_arr, seed_provided):
    random.seed(seed_provided)
    out_byte_arr = bytearray([])
    for byte in byte_arr:
        byte += random.randint(0, 255)
        byte %= 256
        out_byte_arr.append(byte)
    return out_byte_arr

def decrypt_bytes(byte_arr, seed_provided):
    random.seed(seed_provided)
    out_byte_arr = bytearray([])
    for byte in byte_arr:
        byte -= random.randint(0, 255)
        byte += 256
        byte %= 256
        out_byte_arr.append(byte)
    return out_byte_arr

def decrypt(inF, seed_provided, outF):
    random.seed(seed_provided)
    with open(inF, "rb") as readF:
        with open(outF, "wb") as writeF:
            byte_arr = bytearray(readF.read())
            writeF.write(decrypt_bytes(byte_arr, seed_provided))