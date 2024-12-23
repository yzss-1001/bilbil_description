import csv
import time
import requests
def get_minpage(nowpage):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    }
    response = requests.get(f'https://api.bilibili.com/x/v2/reply/main?next={nowpage}&type=1&oid=BV1J4411v7g6&mode=3',
                            headers=headers,
                            timeout=10)
    response.encoding = 'utf-8'
    items = response.json()['data']['replies']
    with open('description_data.csv', 'a', newline='', encoding='utf-8') as f:
        csv_writer = csv.DictWriter(f, fieldnames=['内容','id', '名称', '性别', '经验', '点赞'])
        csv_writer.writeheader()
        n=0
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
            n+=1
        return n


if __name__ == '__main__':
    total=0
    print("请输入你要爬取的页数:", end='')
    Numberpage = int(input())
    for nowpage in range(Numberpage):
        total = total+get_minpage(nowpage)
        print(f"爬取条数:{total}")
    print(f"共爬取{total}条信息")

