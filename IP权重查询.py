#!/usr/bin/env python
import requests
import re

def ip_aizhan():
    header = {
        'Host': 'www.aizhan.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.aizhan.com/'
    }

    with open('./IP反查结果.txt', 'r') as f:
            for u in f:
                url='https://dns.aizhan.com/cha/'+u+'/'
                url = url.split()
                url = ''.join(url)
                # print(url)
                try:
                    res = requests.get(url=url,headers=header)
                    res = res.text
                    # print(res)

                
                    aizhan_baidu = re.findall(r'''<li>百度权重：<a id=.*?><img src=.*?alt="(.*)"/></a></li>''', res)
                    aizhan_google = re.findall(r'''<li>谷歌PR：<a id=.*?><img src=.*?alt="(.*)"/></a></li>''', res)
                    baidu =int(aizhan_baidu[0])
                    google = int(aizhan_google[0])


                    if int(aizhan_baidu[0]) >=1 or int(aizhan_google[0]) >=3:
                        
                        # print(aizhan_baidu,aizhan_google)
                        u = u.split()
                        u = ''.join(u)
                        parse = 'url地址:{}  百度权重{}  谷歌权重{}'.format(u,baidu,google)
                        print(parse)
                        with open('域名权重.txt','a',encoding='utf-8') as f:
                            f.write(parse+'\n')
                except:
                    print("fail")

ip_aizhan()