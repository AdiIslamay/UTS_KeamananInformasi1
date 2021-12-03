import hashlib
# mengimport library

plaintext = "jawaraSmart19".encode()
d = hashlib.sha256(plaintext)


hash = d.digest()
print(hash)


hash = d.hexdigest()
print(hash)
