def decode(s):
    lists = [i for i in s.split('0')]
    charlist = [chr(i) for i in range(ord('A'), ord('z') + 1)]
    ret = []
    for i in lists:
        tmp = 0
        for j in range(len(i)):
            tmp += int(i[j])
        ret.append(charlist[tmp - 1])
    return ''.join(ret).lower()

print(decode('884080810882108108821042084010421'))
