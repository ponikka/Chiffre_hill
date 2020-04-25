from Decryption import decryption
from Encryption import encryption

letter = ord('A')
alphabet = {chr(key): value for value, key in enumerate(range(letter, letter + 26))}

kek = encryption('ACT', 'GYBNQKURP', alphabet)
print(kek)