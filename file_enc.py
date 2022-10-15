import encryptor

def encrypt(fileName, seed_provided, newF):
    with open(fileName, "rb") as readF:
        with open(newF, "wb") as writeF:
            byte_arr = bytearray(readF.read())
            writeF.write(encryptor.encrypt_bytes(byte_arr, seed_provided))
            
def decrypt(inF, seed_provided, outF):
    with open(inF, "rb") as readF:
        with open(outF, "wb") as writeF:
            byte_arr = bytearray(readF.read())
            writeF.write(encryptor.decrypt_bytes(byte_arr, seed_provided))