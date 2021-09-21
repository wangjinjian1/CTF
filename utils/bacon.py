letters1 = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
]
letters2 = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
]
cipher1 = [
    "aaaaa", "aaaab", "aaaba", "aaabb", "aabaa", "aabab", "aabba",
    "aabbb", "abaaa", "abaab", "ababa", "ababb", "abbaa", "abbab",
    "abbba", "abbbb", "baaaa", "baaab", "baaba", "baabb",
    "babaa", "babab", "babba", "babbb", "bbaaa", "bbaab",
]
cipher2 = [
    "AAAAA", "AAAAB", "AAABA", "AAABB", "AABAA", "AABAB", "AABBA",
    "AABBB", "ABAAA", "ABAAA", "ABAAB", "ABABA", "ABABB", "ABBAA",
    "ABBAB", "ABBBA", "ABBBB", "BAAAA", "BAAAB", "BAABA",
    "BAABB", "BAABB", "BABAA", "BABAB", "BABBA", "BABBB",
]


def bacon1(string):
    lists = []
    # 分割，五个一组
    for i in range(0, len(string), 5):
        lists.append(string[i:i+5])
    # print(lists)
    # 循环匹配，得到下标，对应下标即可
    for i in range(0, len(lists)):
        for j in range(0, 26):
            if lists[i] == cipher1[j]:
                # print(j)
                print(letters1[j], end="")
    print("")


def bacon2(string):
    lists = []
    # 分割，五个一组
    for i in range(0, len(string), 5):
        lists.append(string[i:i+5])
    # print(lists)
    # 循环匹配，得到下标，对应下标即可
    for i in range(0, len(lists)):
        for j in range(0, 26):
            if lists[i] == cipher2[j]:
                # print(j)
                print(letters2[j], end="")
    print("")
