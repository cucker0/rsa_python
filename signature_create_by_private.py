"""
使用 RSA 私钥创建消息摘要的签名

即 使用 RSA 私钥对 消息摘要值 进行 加密
"""

import base64
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5

private_key_file = './private.pem'
msg_file = './message2.txt'
msg_signature_file = './message2_signature.bin'

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


# 添加签名
def create_rsa_signature(message: str) -> str:
    """ 对消息进行签名

    本质是对消息的摘要进行签名

    :param message: str
        要进行签名的消息
    :return: str
        返回 base64 加密后的 签名
    """
    private_key = read_file(private_key_file, 'r')
    rsa_key = RSA.importKey(private_key)
    signer = Signature_pkcs1_v1_5.new(rsa_key)
    # 1. 消息 HASH 摘要生成器
    hash_obj = SHA256.new()
    # 2. 生成消息的 HASH 摘要
    hash_obj.update(message.encode(encoding='utf-8'))
    # 3. 生成签名
    sign = signer.sign(hash_obj)  # 数据类型为 bytes
    # 4. base64 加密 签名
    signature = base64.b64encode(sign)
    return signature.decode('utf-8')

if __name__ == '__main__':
    message = read_file(msg_file)
    # 相同的 message，每次生成的 签名 都相同。
    signature = create_rsa_signature(message)
    print(signature)
    with open(msg_signature_file, 'w') as f:
        f.write(signature)
    print(f'{msg_file} 文件签名完成，签名文件为：{msg_signature_file}')