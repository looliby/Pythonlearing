import re
import requests  # request库用于获取网络资源


def getHtml(url):  # 获取网址为url的网页
    fakeHeaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)  \ AppleWebKit/537.36  (KHTML,like,Gecko)  \ '
                      'Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.77',
        'Accept': 'text/html,application/xhtml+xml,*/*'}
    # 伪装浏览器发送请求
    try:
        r = requests.get(url, headers=fakeHeaders)
        r.encoding = r.apparent_encoding  # 确保网页编码正确
        return r.text  # 返回值是个字符串，内容是整个页面内容
    except Exception as e:
        print(e)
        return ""


def getBaiduPictures(word, n):  # 下载n个百度图片搜来的关于word的图片保存到本地
    url = "https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word="
    url += word
    html = getHtml(url)
    pt = '\"objURL\":.*?src=(.*?)&'  # 正则表达式，用于寻找图片地址
    i = 0
    for x in re.findall(pt, html):
        x = x.replace("%3A", ":")
        x = x.replace("%2F", "/")
        if not (x.lower().endswith(".jpg")) or x.lower().endswith(".jpeg") or x.lower().endswith(".png"):
            continue  # 只获取后缀名为jpg,jpeg,png的图片文件
        try:
            r = requests.get(x, stream=True)  # 获取x对应的网络资源
            pos = x.rfind(".")  # 处理后缀名
            f = open('D:\\Python_test\\temp1\\{0}{1}{2}'.format(word, i, x[pos:]), "wb")  # "wb"表示二进制写方式打开文件
            f.write(r.content)  # 图片内容写入文件
            f.close()
            print(x)
            i += 1
        except Exception as e:
            pass
        if i >= n:
            break


getBaiduPictures("熊猫", 5)
