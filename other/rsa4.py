from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import binascii

# 加载私钥，这里需要你提供私钥文件的路径和密码（如果有的话）
private_key_file = '/data/key_peer/private.pem'
signature_file = '/data/key_peer/signature_msg.sign'

with open(private_key_file, 'rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

# 这里是你的签名内容，通常是二进制数据
# encrypted_signature = b'...'

with open(signature_file, 'rb') as sign_file:
    encrypted_signature = sign_file.read()

# 指定RSASSA-PKCS1-v1_5签名算法，这里的hash算法根据你的实际情况选择
signature = private_key.decrypt(
    encrypted_signature,
    padding.PKCS1v15()
)

with open('/data/key_peer/msg.txt', 'rb') as source_file:
    src_file = source_file.read()

print("解密后的签名:", signature)
print("解密后的签名 转 int:", int.from_bytes(signature, byteorder='big', signed=False))
print("源文件：", src_file)
