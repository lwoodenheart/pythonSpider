"""
下载百度图片里的所有图片
"""
import requests
import re
page_url = 'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0'

response = requests.get(page_url)
response.encoding = 'utf-8'
html = response.text
# 提取 img_url 正则表达式
imgs = re.findall(r'"thumbURL":"(.*?)"', html)

for index, img_url in enumerate(imgs):

    # img_url = 'http://img5.imgtn.bdimg.com/it/u=2198746125,2255961738&fm=26&gp=0.jpg'
    # 图片防盗链 伪装
    headers = {
        'Referer': 'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0'
    }
    # 发送请求
    response = requests.get(img_url, headers=headers)
    # print(response.content)
    # 写到文件
    with open('%s.%s' % (index, img_url.split('.')[-1]), 'wb') as f:
        f.write(response.content)