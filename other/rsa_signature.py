"""
pow() 参考 https://docs.python.org/3/library/functions.html#pow

# pow(base, exp, mod=None)

1. 如果 mod 为 None，即 pow(base, exp)，则返回 base 的 exp 次方，也就是 base**exp
2. 如果 mod 存在(mod 不为 None)，且 exp > 0 的正数，则返回 base 的 exp 次方 再 模以 mod。结果等于 pow(base, exp) % mod， 但计算效率要比后者高。
注意：如果 base、exp 为 整数，且存在 mod，则 mod 必须为 非 0 的整数。

3. 如果 mod 存在，且 exp 为负数，则 base 与 mod 必须互为质数，且 base、mod 均为整数，也就是下面这种情况：
pow(inv_base, -exp, mod)
inv：inverse，倒数。
inv_base、mod 必须为整数，且 inv_base 与 mod 互为质数。

>>> pow(38, -1, mod=97)
23
>>>(23 * 38) % 97 == 1
True

(x * 38) % 97 == 1

设 pow(38, -1, mod=97) 结果为 x，则有方程
38x == 97n + 1    （n 为 >=0 的整数）
当 n = 9 时，解得 x = 23

通用方程，设结果 为 x，则有
(x * inv_base) % mod == 1，
或
inv_base * x = mod * n + 1  （n 为 >=0 的整数）
"""

# Requer pycryptodome
# pip install pycryptodome

from Crypto.PublicKey import RSA

# Generate RSA key
keyPair = RSA.generate(bits=1024)
print(f"Public key:  (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")

# RSA sign the message
msg = b'A message for signing'
from hashlib import sha512

hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
signature = pow(hash, keyPair.d, keyPair.n)
print("Signature:", hex(signature))

# RSA verify signature
msg = b'A message for signing'
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
print("Signature valid:", hash == hashFromSignature)


# RSA verify signature (tampered msg)
msg = b'A message for signing (tampered)'
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
print("Signature valid (tampered):", hash == hashFromSignature)