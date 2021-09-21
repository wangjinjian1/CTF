import requests,unicodedata
a='11 111 010 000 0 1010 111 100 0 00 000 000 111 00 10 1 0 010 0 000 1 00 10 110'
b=a.replace('1','-').replace('0','.').replace(' ','/')
print(b)
s='&#76;'
line = unicodedata.normalize('NFKD',s).encode('ascii','ignore')
print(line)
print(s.encode().decode('unicode-escape'))
print(chr(76))
print(ord('z'))
