import json,os

def read_json_file(dir):
    try:
        f = open(dir,encoding='utf-8')
        lines = f.readlines()
        for i in lines:
            lpname = json.loads(i)['lpname']
            trend = json.loads(i)['trend']
            data = trend.split('&')[0]
            title = trend.split('&')[1].strip()
            # 此时的文本串不知道如何处理
            pass
    except Exception as ex:
        print(ex)

dir = r'E:\xsq\test\PycharmProjects\scrapy-FangTX\FangTX\sources\data-2018-04-19.json'
read_json_file(dir.replace('\\','/'))