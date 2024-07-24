"""
使用 RSA 私钥解密数据
"""

import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5

private_key_file = './private.pem'
msg_encrypt_file = './message_encrypt.bin'

def read_file(file_path, mode='r') -> str:
    """ 读取指定的文件

    :param file_path: str
        path of ther file
    :param mode: str
        mode of open file,
        default is 'r',
        options: 'r', 'rb'
    :return: str
        返回读取的文件内容
    """
    # with open() as f 下次读取时，会使用上次打开的 文件句柄
    # with open(public_key_file, mode) as f:
    #     return f.read()

    f = open(file_path, mode, encoding='utf-8')
    data = f.read()
    f.close()
    return data


# RSA 解密
def rsa_decrypt(cipher_text: str):
    """ RSA 解密

    :param cipher_text: str
        要解密的数据
    :return: str
        返回解密的数据
    """
    private_key = read_file(private_key_file, 'r')
    # 1. base64 解密
    decode_text = base64.b64decode(cipher_text)
    # tips --start
    # RSA.importKey(private_key) is a RsaKey,
    # from Crypto.PublicKey.RSA import RsaKey
    # tips --end
    rsa_key = RSA.importKey(private_key)
    cipher = Cipher_pkcs1_v1_5.new(rsa_key)  # 创建用于执行 pkcs1_v1_5 加密 或 解密 的密码
    # 2. RSA 解密
    decrypt_text = cipher.decrypt(decode_text, b'rsa')
    return decrypt_text.decode('utf-8')

if __name__ == '__main__':
    encrypt_data = read_file(msg_encrypt_file, 'r')
    result = rsa_decrypt(encrypt_data)
    # result 的值 与 文件 ./message.txt 相同
    print(result)