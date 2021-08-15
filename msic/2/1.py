from PIL import Image
import base64
def func(length, path):
    im = Image.open(path)
    width = im.size[0]
    height = im.size[1]
    length*=8
    b = ''
    count = 0
    for i in range(height):
        for j in range(width):
            pixel = im.getpixel((j, i))
            for h in range(3):
                if count % 3 == h:
                    tmp = int(pixel[h])
                    b += str(divmod(tmp,2)[1])
                    count += 1
                    if count == length:
                        break
            if count == length:
                break
        if count == length:
            break
    result = ''
    for i in range(0, len(b), 8):
        result += chr(int(b[i:i + 8], 2))
    return result

res=func(52,'txt.bmp')
print(base64.b64decode(res))
