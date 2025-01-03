import pymysql
import csv
import time
import requests
db = pymysql.connect(host='localhost',port=3306,user='root',password='',db='bilbil_data',charset='utf8')
cursor = db.cursor()

def insertDB(content, id, name,sex,experience,like_number):
    #插入数据
    try:
        sql = "insert into description_data values ('%s','%s','%s','%s','%s','%s')" % (content, id, name,sex,experience,like_number)
        cursor.execute(sql)
        db.commit()
    #打印错误
    except Exception as e:
        db.rollback()
        print(e)

def get_minpage(nowpage):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    }
    # time.sleep(0.1)
    response = requests.get(f'https://api.bilibili.com/x/v2/reply/main?next={nowpage}&type=1&oid=BV1pJ411P7zm&mode=3',
                            headers=headers,
                            timeout=10)
    response.encoding = 'utf-8'
    items = response.json()['data']['replies']
    n=0
    for item in items:
        insertDB(item['content']['message'],
                 item['member']['mid'],
                 item['member']['uname'],
                 item['member']['sex'],
                 item['member']['rank'],
                 item['like'])
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





