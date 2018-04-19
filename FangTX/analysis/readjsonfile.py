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
