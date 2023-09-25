#!/usr/bin/env python
import requests
import re

def ip_recerse():
    header = {
        'Host': 'dns.aizhan.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://dns.aizhan.com/'
    }
    
    with open('./url.txt', 'r') as f:
        for u in f:
            url='https://dns.aizhan.com/'+u+'/'
            url = url.split()
            url = ''.join(url)
            # print(url)

            try:
                res = requests.get(url=url,headers=header)
                res = res.text
                aizhan_nums = re.findall(r'''<span class="red">(.*?)</span>''', res)
                if int(aizhan_nums[0]) > 0:
                    aizhan_domains = re.findall(r'''rel="nofollow" target="_blank">(.*?)</a>''', res)
                    # print(aizhan_domains)
                    with open('IP反查结果.txt','a',encoding='utf-8') as f:
                        for us in aizhan_domains:
                            print(us)
                            f.write(us+'\n')
                            
            except:
                print('fail')

ip_recerse()

    