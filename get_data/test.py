from sphinx.util import requests

cookies = {
    'buvid3': 'A02E7647-6DFD-E7ED-47C4-7472A53A74A535400infoc',
    'b_nut': '1727598635',
    '_uuid': '16375F45-C5DB-F3CA-A989-10D6ACF105C76E35219infoc',
    'enable_web_push': 'DISABLE',
    'buvid4': '4701039C-803D-911B-0440-90D565BD80EB36583-024092908-fcASUcpyhjGK9py2pG6QZA%3D%3D',
    'buvid_fp': '7ebe15a912a3b9d49babbd065651ccd9',
    'rpdid': "|(k|JJumY|lY0J'u~k~lm)Yll",
    'DedeUserID': '3546637194496604',
    'DedeUserID__ckMd5': '75eeaf6bb69fc726',
    'header_theme_version': 'CLOSE',
    'bp_t_offset_3546637194496604': '1012860950342008832',
    'home_feed_column': '4',
    'b_lsid': '594817A2_193F0FBE1C0',
    'browser_resolution': '1243-727',
    'bili_ticket': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzUxNzQwNjAsImlhdCI6MTczNDkxNDgwMCwicGx0IjotMX0.8rPctKAg5ewlY2_FcZ057wjijwxtoS9Y2a4_Mq2mK3k',
    'bili_ticket_expires': '1735174000',
    'SESSDATA': '1a360919%2C1750466861%2C71931%2Ac1CjBmFaDkF-fOgu1PpOJcBFKRr8dR0Rv0_cva6fFfU5LDofurdQ6BFZXyyRkI6AqPd28SVjJVbFYyTVVzNnZEZkd2Y1JHeW1lWE9BQmM5VkZqbkY4S2F3eThQeUp1Z1V6cHJVZjQ1XzUtbkg0NXlNTS1XSmFIZTd5Nm1jeEI1ZXV2aWgxN0JrYVRRIIEC',
    'bili_jct': 'e1253394c983349ef542d6c2149f3be0',
    'sid': '6dob8aj3',
    'CURRENT_FNVAL': '4048',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'cookie': "buvid3=A02E7647-6DFD-E7ED-47C4-7472A53A74A535400infoc; b_nut=1727598635; _uuid=16375F45-C5DB-F3CA-A989-10D6ACF105C76E35219infoc; enable_web_push=DISABLE; buvid4=4701039C-803D-911B-0440-90D565BD80EB36583-024092908-fcASUcpyhjGK9py2pG6QZA%3D%3D; buvid_fp=7ebe15a912a3b9d49babbd065651ccd9; rpdid=|(k|JJumY|lY0J'u~k~lm)Yll; DedeUserID=3546637194496604; DedeUserID__ckMd5=75eeaf6bb69fc726; header_theme_version=CLOSE; bp_t_offset_3546637194496604=1012860950342008832; home_feed_column=4; b_lsid=594817A2_193F0FBE1C0; browser_resolution=1243-727; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzUxNzQwNjAsImlhdCI6MTczNDkxNDgwMCwicGx0IjotMX0.8rPctKAg5ewlY2_FcZ057wjijwxtoS9Y2a4_Mq2mK3k; bili_ticket_expires=1735174000; SESSDATA=1a360919%2C1750466861%2C71931%2Ac1CjBmFaDkF-fOgu1PpOJcBFKRr8dR0Rv0_cva6fFfU5LDofurdQ6BFZXyyRkI6AqPd28SVjJVbFYyTVVzNnZEZkd2Y1JHeW1lWE9BQmM5VkZqbkY4S2F3eThQeUp1Z1V6cHJVZjQ1XzUtbkg0NXlNTS1XSmFIZTd5Nm1jeEI1ZXV2aWgxN0JrYVRRIIEC; bili_jct=e1253394c983349ef542d6c2149f3be0; sid=6dob8aj3; CURRENT_FNVAL=4048",
    'origin': 'https://www.bilibili.com',
    'priority': 'u=1, i',
    'referer': 'https://www.bilibili.com/video/BV1AM4y1M71p/?spm_id_from=333.337.search-card.all.click&vd_source=c299956f432211c93b9ab22b9000b695',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
}

response = (requests.get('https://api.bilibili.com/x/v2/reply/wbi/main?oid=931463745&type=1&mode=3&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=990128abe73c51955170f3d289a05cb3&wts=1734914949',cookies=cookies,headers=headers,))
response.encoding = 'utf-8'
items = response.json()['data']['replies']
for item in items:
    print(item['content']['message'])
    print(item['member']['mid'])
    print(item['member']['uname'])
    print(item['member']['sex'])
    print(item['member']['rank'])
    print(item['like'])
    break