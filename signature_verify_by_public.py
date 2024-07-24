"""
使用 公钥 验证 签名

"""

import base64
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5

public_key_file = './public.pem'
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


# 验证签名
def verify_signature(message: str, signature: str, public_key: str) -> bool:
    """ 验证签名

    :param message: str
        消息（未加密的消息）
    :param signature: str
        签名内容
    :param public_key: str
        公钥字符串值
    :return: bool
        验证是否通过
        True: 验证签名通过
        False: 验证签名失败
    """

    # 1. 消息 HASH 摘要生成器
    hash_obj = SHA256.new()
    # 2. 生成消息的 HASH 摘要
    hash_obj.update(message.encode(encoding='utf-8'))
    # 3. 签名的内容
    # 因为生成的签名，再用 base64 加密了，所以需要先 base64 解密。base64 加密、解密是可逆的。
    signature_text = base64.b64decode(signature)

    # 3. 创建一个 验证器
    rsa_key = RSA.importKey(public_key)
    verifier = Signature_pkcs1_v1_5.new(rsa_key)

    is_verify = verifier.verify(hash_obj, signature=signature_text)
    return is_verify

if __name__ == '__main__':
    public_key = read_file(public_key_file, 'r')
    message = read_file(msg_file, 'r')
    signature = read_file(msg_signature_file, 'r')
    result = verify_signature(message, signature, public_key)
    print(result)