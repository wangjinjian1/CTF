flag='flag{}'
xman='XMAN{}'
cyberpeace='cyberpeace{}'
def masonic():
    ans=xman.format('{the answer is false}')
    print(ans)
    return ans

def flag_in_your_hand():
    ans='RenIbyd8Fgg5hawvQm7TDQ'
    print(ans)
    return ans
#8842101220480224404014224202480122
def mishujiami():
    a = ["88421", "0122", "048", "02244", "04", "0142242", "0248", "0122"]
    flag = ""
    for j in range(0, len(a)):
        str = a[j]
        list = []
        sum = 0
        for i in str:
            list.append(i)
        length = len(list)
        for i in range(0, length):
            sum += int(list[i])
        flag += chr(64 + sum)
    print(cyberpeace.format('{'+flag+'}'))
    return cyberpeace.format('{'+flag+'}')

def hunhebianma():
    char='/119/101/108/99/111/109/101/116/111/97/116/116/97/99/107/97/110/100/100/101/102/101/110/99/101/119/111/114/108/100'
    arr1=char.split('/')
    arr=[chr(int(i)) for i in arr1 if i!='']
    print(cyberpeace.format('{'+''.join(arr)+'}'))
    return cyberpeace.format('{'+''.join(arr)+'}')

def bmorse():
    print('cyberpeace{attackanddefenceworldisinteresting}')
    return 'cyberpeace{attackanddefenceworldisinteresting}'
#11 111 010 000 0 1010 111 100 0 00 000 000 111 00 10 1 0 010 0 000 1 00 10 110

#Y3liZXJwZWFjZXtXZWxjb21lX3RvX25ld19Xb3JsZCF9
def base64():
    import base64
    s=base64.b64decode('Y3liZXJwZWFjZXtXZWxjb21lX3RvX25ld19Xb3JsZCF9').decode()
    print(s)
    return s

def lihua():
    print('15CCLiHua')
    return '15CCLiHua'

def yanjianfeishi():
    print('flag{F1@g}')

def secret():
    print('flag{ssctf_@seclover%coffee_*}')

def nizhidao():
    print('keyis{sec1over%_6ugscan_@coffee}')

def simplegif():
    s='0101100001001101010000010100111001111011001110010011011000110101001101110011010101100010011001010110010101100100001101000110010001100101011000010011000100111000011001000110010101100100001101000011011100110011001101010011011000110100001100110110000101100101011000110110011001100001001100110011010101111101'
    ans=''
    for i in range(0,8):
        temp=int(s[i:i+8],2)
        print(temp)
        ans+=chr(temp)
    print('XMAN{96575beed4dea18ded4735643aecfa35}')

def mysql():
    print('71e55075163d5c6410c0d9eae499c977')

def misc100():
    print('XMAN{Png_HIde_sEcret}')

def misc200():
    str = [
        122,
        104,
        105,
        95,
        102,
        117,
        95,
        115,
        97,
        105,
        95,
        110,
        105,
        110,
        103]
    flag1 = ''
    for i in str:
        flag1 += chr(i)
    print(flag.format('{'+flag1+'}'))
#2333
def morse():
    print('flag{MORSECODEISSOINTERESTING}')

def shenqi():
    print('lctf{6d3677dd}')

#oknqdbqmoq{kag_tmhq_xqmdzqp_omqemd_qzodkbfuaz}
def ceasar():
    print('cyberpeace{you_have_learned_caesar_encryption}')

def easyrsa():
    import gmpy2
    p = 473398607161
    q = 4511491
    e = 17
    phi = (p - 1) * (q - 1)
    # 计算得到私钥（n, d）
    d = int(gmpy2.invert(e, phi))
    print(d)
#00 00 00 00 49 45 4E 44 AE 60 82
#89 50 4E 47 OD 0A 1A 0A
def magical():
    print('XMAN{513a2842b9b38ff42ed92b874e075f28}')

def hong():
    print('BCTF{cute&fat_cats_does_not_like_drinking}')

def light():
    print('Gaussian_elimination_is_awesome!')
    return 'RCTF{Gaussian_elimination_is_awesome!}'

def intoU():
    print('RCTF{bmp_file_in_wav}')

def message():
    print('RCTF{ArEciBo_mEsSaGe}')

def icant():

    return
def simplerar():
    print('flag{yanji4n_bu_we1shi}')

#pkcrack -C fl4g.zip -c plaintext.txt  -p plaintext.txt -d decrypt.zip
def flagflagflag():

    return
def rulai13():
    print('flag{bdscjhbkzmnfrdhbvckijndskvbkjdsab}')

def xiezhuozi():
    print(flag.format('{'+'hjzcydjzbjdcjkzkcugisdchjyjsbdfr'+'}'))
    string = "c8e9aca0c6f2e5f3e8c4efe7a1a0d4e8e5a0e6ece1e7a0e9f3baa0e8eafae3f9e4eafae2eae4e3eaebfaebe3f5e7e9f3e4e3e8eaf9eaf3e2e4e6f2"
    string1 = ""
    for i in range(0, len(string), 2):
        string1 += "0x"
        string1 += string[i]
        string1 += string[i + 1]
        string1 += ","
    string1 = string1[:-1]
    string2 = []
    string2 = string1.split(",")
    flag1 = ""
    for i in range(len(string2)):
        flag1 += chr(int(string2[i], 16) - 128)

def pdf():
    print('flag{security_through_obscurity}')

def giveyouflag():
    print('flag{e7d478cf6b915f50ab1277f78502a2c5}')

def stegano():
    print('flag{CONGRATULATIONSFLAG1NV151BL3M3554G3}'.lower())

def babypython():
    print('flag{flag{63fd401cd8e3e3a69556a526cded0df9}}')

def php():
    print('flag{fced7a8ef114d04ce5ca421b6ab52f28}')

def simplephp():
    print('Cyberpeace{647E37C7627CC3E4019EC69324F66C7C}')

def command():
    print('flag{76d4b41a2d70a5bc57ae9210e7666e91}')

def shell():
    print('Cyberpeace{9755FBFF7099C0987DBFC18E20052E87}')

def weak():
    print('Cyberpeace{B8C8C412FB74FE5E9B2FDBD7907E397F}')

def xff():
    print('Cyberpeace{0B224EC36E15BD74B3C63D0583191EF}')

def diable():
    print('flag{a61add771bb90a8c538bb21105f1e698}')

def cookie():
    print('flag{6f53f18c259606e9ff0a966a694aa7fc}')

def backup():
    print('Cyberpeace{855A1C4B3401294CB6604CCC98BDE334}')

def robots():
    print('flag{0206fc063e56bf2d7c22ea04c6312850}')

def post():
    print('Cyberpeace{77968C8A7FC568EF10D4AD9475F8F103}')

def viewsource():
    print('flag{2ff76ccf011689cd387f62d501a9727f}')
if __name__=='__main__':
    easyrsa()

