import re
import requests  # request库用于获取网络资源


def getHtml(url):  # 暂时适用于百度图片搜索
    import asyncio  # Python 3.6之后自带的协程库
    import pyppeteer as pyp
    async def asGetHtml(url):  # 获取url对应网页的源代码
        browser = await pyp.launch(headless=False,
                                   executablePath="C:/Users/SLO walk/Downloads/chromium-sync/chrome-win32/chrome.exe")
        # 启动Chromium，browser即为Chromium浏览器，非隐藏启动
        page = await browser.newPage()  # 在浏览器打开一个新页面
        await page.setUserAgent('Mozilla/5.0 (Windows NT 6.1; Win64; \ x64) AppleWebKit/537.36 (KHTML, like Geckko) \
                                Chrome/78.0.3904.70 Safari/537.36')  # 反反爬措施
        await page.evaluateOnNewDocument('() =>{ Object.defineProperties(navigator, \
                                         { webdriver:{ get: () => false } }) }')  # 反反爬措施
        await page.goto(url)  # 装入url对应的网页
        text = await page.content()  # page.content就是网页源代码字符串
        await browser.close()  # 关闭浏览器
        return text
    m = asyncio.ensure_future(asGetHtml(url))  # 协程外启动协程
    asyncio.get_event_loop().run_until_complete(m)  # 等待协程结束
    return m.result()  # 返回的就是asGetHtml的返回值 text


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


getBaiduPictures("猫", 5)
