m = input("Input message to decrypt: ")
lenM = len(m)
k = input("Input decryption key: ")

m = m.encode()
k = k.encode()

m = int.from_bytes(m, "little")
k = int.from_bytes(k, "little")

o = m ^ k
print((o.to_bytes(lenM, "little")).decode())