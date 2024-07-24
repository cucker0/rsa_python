"""
使用 RSA 公钥加密数据
"""

import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5

public_key_file = './public.pem'
msg_file = './message.txt'
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


# RSA 加密
def rsa_encrypt(message: str):
    """使用 RSA 公钥加密消息

    :param message: str
        需要加密的消息
    :return:
    """
    public_key = read_file(public_key_file)
    # tips --start
    # RSA.importKey(private_key) is a RsaKey,
    # from Crypto.PublicKey.RSA import RsaKey
    # tips --end
    rsa_key = RSA.importKey(public_key)
    cipher = Cipher_pkcs1_v1_5.new(rsa_key)  # 创建用于执行 pkcs1_v1_5 加密 或 解密 的密码
    # 1. 先 rsa 加密，2. 再进行 base64 加密
    # type of cipher_text is byte array
    cipher_text = base64.b64encode(cipher.encrypt(message.encode('utf-8')))
    # return cipher_text.decode('utf-8')  # type: str
    return cipher_text

if __name__ == '__main__':

    msg = read_file(msg_file)
    result = rsa_encrypt(msg)  # 每次加密的结果不一样
    # print(result)
    with open(msg_encrypt_file, 'wb') as f:
        f.write(result)
    print(f'{msg_file} 文件加密完成.')