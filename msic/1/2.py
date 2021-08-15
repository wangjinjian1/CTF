dict = {}
for i in range(4, 30):
    dict[i] = chr(i + 61)
for i in range(30, 39):
    dict[i] = chr(i + 19)
dict[39] = '0'
nums = []
with open('2.text', 'r') as f:
    for key in f.readlines():
        nums.append(int(key[6:8], 16))
output = ''
for num in nums:
    if num == 0:
        continue
    else:
        output += dict[num]

