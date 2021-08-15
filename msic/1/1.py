f1 = open('1.text', 'r')
f2 = open('2.text', 'w+')
for s in f1.readlines():
    temp = s.strip()
    if s.strip():
        for i in range(0, len(temp), 2):
            if i + 2 == len(temp):
                out = temp[i:i + 2]
            else:
                out = temp[i:i + 2] + ':'
            f2.write(out)
        f2.write('\n')
    else:
        continue
f2.close()
f1.close()