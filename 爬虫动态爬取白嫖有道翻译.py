import requests
import json
def do (word):  
        url = "http://fanyi.youdao.com/translate?smartresult=dict&"
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41"}
        data = {
                'i' : word,
                'from' : 'AUTO',
                'to' : 'AUTO',
                'smartresult' : 'dict',
                'client' : 'fanyideskweb',
                'salt' : '16096771607986',
                'sign' : 'e72a9ef79c90a05a621157815772b913',
                'lts' : '1609677160798',
                'bv' : '4f7ca50d9eda878f3f40fb696cce4d6d',
                'doctype' : 'json',
                'version' : '2.1',
                'keyfrom' : 'fanyi.web',
                'action' : 'FY_BY_REALTlME',
                }
        response = requests.post(url=url,data=data,headers=header).content.decode()
        res = json.loads(response)
        print(res['translateResult'][0][0]['tgt'])
        print('*'*50)
while True:
        word = input('请输入想翻译的单词或句子：')
        do(word)
        a = int(input("是否继续翻译，是/否：0/1："))
        if a==0:
                pass
        else:
                break
