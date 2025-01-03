import csv
import time
import requests

def get_bv(video_nowpage, content):
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
        'home_feed_column': '4',
        'bili_ticket': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzU0NTM1OTMsImlhdCI6MTczNTE5NDMzMywicGx0IjotMX0.AD3Up80gLFE3FCNtFw09MG3t1nOY6lumUCoXy7XHnlE',
        'bili_ticket_expires': '1735453533',
        'SESSDATA': '26837eb1%2C1750746394%2C54b5d%2Ac1CjBSGGTeq62asvIgPkSceRx4Zo1rZntKjOT9h3xtGH4-pmBbT5kRvMtftj9Ms23vLCwSVkFpZ1dYVTlqZFJPbVZZLVVzNTZYdTY0N0ctNFN4b1Fod0tRRlJXN0RJRTR1ajhRZlduY1pqWWxSQ1RJRzdOeEEzYzdFRVhfb1VkMGpCQXlBYU5DdjJ3IIEC',
        'bili_jct': '92ca7f2869ceb41ff3122f4df824220c',
        'b_lsid': '51DE4A4D_19406224A0C',
        'browser_resolution': '1280-727',
        'bp_t_offset_3546637194496604': '1015464696955797504',
        'sid': '548stnk9',
        'CURRENT_FNVAL': '2000',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        # 'cookie': "buvid3=A02E7647-6DFD-E7ED-47C4-7472A53A74A535400infoc; b_nut=1727598635; _uuid=16375F45-C5DB-F3CA-A989-10D6ACF105C76E35219infoc; enable_web_push=DISABLE; buvid4=4701039C-803D-911B-0440-90D565BD80EB36583-024092908-fcASUcpyhjGK9py2pG6QZA%3D%3D; buvid_fp=7ebe15a912a3b9d49babbd065651ccd9; rpdid=|(k|JJumY|lY0J'u~k~lm)Yll; DedeUserID=3546637194496604; DedeUserID__ckMd5=75eeaf6bb69fc726; header_theme_version=CLOSE; home_feed_column=4; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzU0NTM1OTMsImlhdCI6MTczNTE5NDMzMywicGx0IjotMX0.AD3Up80gLFE3FCNtFw09MG3t1nOY6lumUCoXy7XHnlE; bili_ticket_expires=1735453533; SESSDATA=26837eb1%2C1750746394%2C54b5d%2Ac1CjBSGGTeq62asvIgPkSceRx4Zo1rZntKjOT9h3xtGH4-pmBbT5kRvMtftj9Ms23vLCwSVkFpZ1dYVTlqZFJPbVZZLVVzNTZYdTY0N0ctNFN4b1Fod0tRRlJXN0RJRTR1ajhRZlduY1pqWWxSQ1RJRzdOeEEzYzdFRVhfb1VkMGpCQXlBYU5DdjJ3IIEC; bili_jct=92ca7f2869ceb41ff3122f4df824220c; b_lsid=51DE4A4D_19406224A0C; browser_resolution=1280-727; bp_t_offset_3546637194496604=1015464696955797504; sid=548stnk9; CURRENT_FNVAL=2000",
        'origin': 'https://search.bilibili.com',
        'priority': 'u=1, i',
        'referer': 'https://search.bilibili.com/all?keyword=%E8%94%A1%E5%BE%90%E5%9D%A4&from_source=webtop_search&spm_id_from=333.1007&search_source=3&page=3&o=48',
        'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    }

    params = {
        'category_id': '',
        'search_type': 'video',
        'ad_resource': '5654',
        '__refresh__': 'true',
        '_extra': '',
        'context': '',
        'page': f'{video_nowpage + 1}',
        'page_size': '42',
        'pubtime_begin_s': '0',
        'pubtime_end_s': '0',
        'from_source': '',
        'from_spmid': '333.337',
        'platform': 'pc',
        'highlight': '1',
        'single_column': '0',
        'keyword': f'{content}',
        'qv_id': 'zZgHludA8aeiyet7sye0PtHwNQXwLOxr',
        'source_tag': '3',
        'gaia_vtoken': '',
        'dynamic_offset': '48',
        'web_location': '1430654',
        'w_rid': '5acad82d18196d102454e3c6608e6ba6',
        'wts': '1735270898',
    }

    response = requests.get(
        'https://api.bilibili.com/x/web-interface/wbi/search/type',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    response.encoding = 'utf-8'
    items = response.json()['data']['result']
    n = 0
    i = 1
    for item in items:
        print(item['bvid'])
        if item['bvid'] == "":  # 防止爬取空bv
            continue
        print(f"爬取第{i}个bv")
        time.sleep(3)
        i += 1
        num = 0
        check = []
        while (True):
            n = n + get_description(num, item['bvid'],video_nowpage,i)
            check.append(n)
            print(f"第{video_nowpage + 1}页爬取条数:{n}")
            print(num)
            if check[num] == check[num - 1] and num >= 1:  # 检测爬到最大评论页数
                break
            num += 1
    return n


def get_description(now_description, bv,video_nowpage,i):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    }

    response = requests.get(f'https://api.bilibili.com/x/v2/reply/main?next={now_description}&type=1&oid={bv}&mode=3',
                            # 视频bv号决定评论对应的视频
                            headers=headers)

    response.encoding = 'utf-8'
    try:
        items = response.json()['data']['replies']
    except KeyError:
        return 0

    with open('../data_save/description.csv', 'a', newline='', encoding='utf-8') as f:
        csv_writer = csv.DictWriter(f, fieldnames=['内容', 'id', '名称', '性别', '经验', '点赞'])
        if video_nowpage==0 and now_description==0 and i==2:#第一次爬取才写表头,防止表头重复。
            csv_writer.writeheader()
        n = 0
        for item in items:
            dit = {
                '内容': item['content']['message'],
                'id': item['member']['mid'],
                '名称': item['member']['uname'],
                '性别': item['member']['sex'],
                '经验': item['member']['rank'],
                '点赞': item['like']
            }
            csv_writer.writerow(dit)
            n += 1
        return n


if __name__ == '__main__':
    total = 0
    print("请输入你要爬取的网页数:", end='')
    Numberpage = int(input())
    print("请输入你要爬取的内容:", end='')
    content = input()
    for video_nowpage in range(Numberpage):
        total = total + get_bv(video_nowpage, content)
        print(f"爬取完第{video_nowpage + 1}个页面:")
    print(f"共爬取评论条数:{total}")
