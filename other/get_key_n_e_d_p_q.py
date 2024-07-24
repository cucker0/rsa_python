from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

private_key_file= '../private.pem'

with open(private_key_file, 'rb') as key_file:
    private_key = serialization.load_pem_private_key(data=key_file.read(), password=None)
    #private_key = serialization.load_pem_private_key(data=key_file.read(), password=b'password_for_open_private_key')

n = private_key.public_key().public_numbers().n
e = private_key.public_key().public_numbers().e
d = private_key.private_numbers().d
p = private_key.private_numbers().p
q = private_key.private_numbers().q

print("N:", n)
print("E:", e)
print("D:", d)
print("P:", p)
print("Q:", q)

