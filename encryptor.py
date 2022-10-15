import random

def encrypt(fileName, seedProvided, newF):
    random.seed(seedProvided)
    byte_arr = bytearray([])
    with open(fileName, "rb") as readF:
        with open(newF, "wb") as writeF:
            while (byte := readF.read(1)):
                int_rep = int.from_bytes(byte, "big")
                int_rep += random.randint(0, 255)
                int_rep %= 256
                byte_arr.append(int_rep)
            writeF.write(byte_arr)

def decrypt(inF, seedProvided, outF):
    random.seed(seedProvided)
    byte_arr = bytearray([])
    with open(inF, "rb") as readF:
        with open(outF, "wb") as writeF:
            while (byte := readF.read(1)):
                int_rep = int.from_bytes(byte, "big")
                int_rep -= random.randint(0, 255)
                int_rep += 256
                int_rep %= 256
                byte_arr.append(int_rep)
            writeF.write(byte_arr)