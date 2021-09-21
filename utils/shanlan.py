import math


def buwei(encrypted_str,fence_length):    # 比如 14，4
    str_len = len(encrypted_str)
    fence_count = math.ceil(str_len/ fence_length)   # 得出4
    target_length = fence_count*fence_length
    jiequ = []
    while str_len<target_length:
        encrypted_str = encrypted_str + '*'
        jiequ.append(encrypted_str[-fence_count :])
        encrypted_str = encrypted_str[:-fence_count]
        str_len += 1

    jiequ.reverse()
    s = ''
    for i in jiequ:
        s = s + i

    result = encrypted_str + s
    return result


def decrypt_fence(encrypted_str,fence_length):
    encrypted_str = buwei(encrypted_str,fence_length)
    if fence_length>=len(encrypted_str) or fence_length<1:
        print("栅栏长度太大或者太小，无需解密")
        return
    fence_count = math.ceil(len(encrypted_str)/fence_length)
    elen=len(encrypted_str)

    # b = elen // f  # 用字符串实际长度除以上面计算出能整出的数字f
    result = {x: '' for x in range(fence_count)}
    for i in range(elen):  # 字符串有多少位，就循环多少次
        a = i % fence_count
        result.update({a: result[a] + encrypted_str[i]})  # 字符串截断，并更新数据
    d = ''
    for i in range(len(result)):
        d += result[i]

    d = d.replace("*", '')
    print(f'假设每栏字数为:{fence_length}，解密结果为：{d}')  # 输出结果，并开始下一个循环


decrypt_fence('flag{ssctf_@seclover%coffee_*}', 15)
