from PIL import Image
im=Image.open('txt.bmp')
print(im.format)
print(im.mode)
pim=im.convert('P')
print(pim.palette)
print(im.info)

a='00000101'
print(int(a,2))
print(chr(97))