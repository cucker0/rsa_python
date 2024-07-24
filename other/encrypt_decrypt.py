"""Here is an example(public key -> (e,n), private key -> (d,n)) using RSA algorithm in python demonstrate:

encrypt using public key, decrypt using private key
encrypt using private key, decrypt using public key
"""

# random prime number
p = 11
# random prime number
q = 47
n = p * q
# random number that is coprime with phi
e = 17
phi = (p - 1) * (q - 1)
# mod_inverse
d = pow(e, -1, phi)

print(d)

# encrypt using public key
enc = pow(123, e, n)
# decrypt using private key
print(pow(enc, d, n))

# encrypt using private key
enc = pow(123, d, n)
# decrypt using public key
print(pow(enc, e, n))
