# encoding: utf-8

import requests

url = "http://www.renren.com/PLogin.do"
data = {"email": "970138074@qq.com", 'password': "pythonspider"}
headers = {"
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

session = requests.Session()

session.post(url, data=data, headers = headers)

response = session.get("http://www.renren.com/880151247/profile")
with open('renren.html', 'w', encoding='utf-8') as f:
    f.write(response.text)