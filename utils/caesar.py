# encoding: utf-8
# encoding: utf-8
"""
@description: 凯撒密码
@author: baola
@time: 2020-06-10 20:14
@file: CaesarCrypto.py
@version: python3.8.morse是摩丝解密的方法
"""

def CaesarEncode(crypto_str, shift):
    """
    凯撒加密
    :param crypto_str: 要加密的明文
    :param shift: 偏移量
    :return: 返回加密后的密文
    """
    result = ""
    num =int(shift)
    for word in crypto_str:
        ch = ord(word)
        if (ord('a') <= ch <= ord('z')):
            ch += num
            if ch > ord('z'):
                ch -= 26

        if (ord('A') <= ch <= ord('Z')):
            ch += num
            if ch > ord('Z'):
                ch -= 26
        result += chr(ch)
    return result

def CaesarDecode(crypto_str, shift):
    """
    凯撒解密
    :param crypto_str: 要解密的密文
    :param shift: 偏移量
    :return: 返回解密后问明文
    """
    result = ""
    num = int(shift)
    for word in crypto_str:
        ch = ord(word)
        if (ord('a') <= ch <= ord('z')):
            ch -= num
            if ch < ord('a'):
                ch += 26

        if (ord('A') <= ch <= ord('Z')):
            ch -= num
            if ch < ord('A'):
                ch += 26
        result += chr(ch)
    return result

#解密：全部遍历
for i in range(1,26):
    print(i,":",CaesarDecode("oknqdbqmoq{kag_tmhq_xqmdzqp_omqemd_qzodkbfuaz}",i))

shift = 0 #偏移量
str = "" #文本
# #解密
# print(CaesarDecode(str,shift))
# #加密
# print(CaesarEncode(str,shift))
