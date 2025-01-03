import csv
import time
import requests
from py2neo import Node, Relationship, Graph, NodeMatcher, RelationshipMatcher
graph = Graph("http://localhost:7474", auth=("neo4j", "a13672937971.."),name="neo4j")
#创建大节点及关系
content_total = Node("content_total",name="内容")
id_total = Node("id_total",name="id")
name_total = Node("name_total",name="名称")
sex_total = Node("sex_total",name="性别")
experience_total = Node("experience_total",name="经验")
like_total = Node("like_total",name="点赞")
graph.create(content_total)
graph.create(id_total)
graph.create(name_total)
graph.create(sex_total)
graph.create(experience_total)
graph.create(like_total)
relationposition1 = Relationship(id_total,'评论',content_total)
relationposition2 = Relationship(id_total,'名称',name_total)
relationposition3 = Relationship(id_total,'性别',sex_total)
relationposition4 = Relationship(id_total,'经验',experience_total)
relationposition5 = Relationship(id_total,'点赞',like_total)
graph.create(relationposition1)
graph.create(relationposition2)
graph.create(relationposition3)
graph.create(relationposition4)
graph.create(relationposition5)
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

    n = 0
    for item in items:
        insert_neo4j(item['content']['message'],item['member']['mid'],item['member']['uname'],item['member']['sex'],item['member']['rank'],item['like'])
        n += 1
    return n



def insert_neo4j(content,id,name,sex,experience,like):
    content = Node("content",content=content)#创建节点
    id = Node("id",id=id)
    name = Node("name",name=name)
    sex = Node("sex",sex=sex)
    experience = Node("experience",experience=experience)
    like = Node("like",like=like)
    graph.create(content)
    graph.create(id)
    graph.create(name)
    graph.create(sex)
    graph.create(experience)
    graph.create(like)


    relationposition1 = Relationship(content_total,'包含',content)
    relationposition2 = Relationship(id_total,'包含',id)
    relationposition3 = Relationship(name_total,'包含',name)
    relationposition4 = Relationship(sex_total,'包含',sex)
    relationposition5 = Relationship(experience_total,'包含',experience)
    relationposition6 = Relationship(like_total,'包含',like)
    graph.create(relationposition1)
    graph.create(relationposition2)
    graph.create(relationposition3)
    graph.create(relationposition4)
    graph.create(relationposition5)
    graph.create(relationposition6)

    relationposition7 = Relationship(id,'评论',content)
    relationposition8 = Relationship(id,'名称',name)
    relationposition9 = Relationship(id,'性别',sex)
    relationposition10 = Relationship(id,'经验',experience)
    relationposition11 = Relationship(id,'点赞',like)
    graph.create(relationposition7)
    graph.create(relationposition8)
    graph.create(relationposition9)
    graph.create(relationposition10)
    graph.create(relationposition11)







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
