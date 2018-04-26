import json,os

def read_json_file_1(dir):
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


# 合并json文件，尚未完成
def merge_json_file(file1,file2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        fc1 = json.load(f1)
        fc2 = json.load(f2)
        fc = fc1.extend(fc2)


def read_json_file_2(dir):
    try:
        header = ['区域','小区', '月份', '价格']
        date = time.strftime("%Y-%m-%d", time.localtime())
        file_dir_name = './' + date + '.csv'
        csvfile = open(file_dir_name, 'wb')
        csvfile.write(codecs.BOM_UTF8)
        csvfile.close()
        csvfile = open(file_dir_name, 'a', newline='', encoding='utf-8')  # 以写入模式打开，如果文件存在，覆盖数据
        writer = csv.DictWriter(csvfile, header)
        # 写入头部，即设置列名
        writer.writeheader()
        item = {}
        highest = {}
        f = open(dir, encoding='utf-8')
        lines = f.readlines()
        for i in lines:
            district = json.loads(i)["result"]["district"]
            lpname = json.loads(i)["result"]["name"]
            trend = json.loads(i)["result"]["data"]
            data = trend.split('&')[0]
            title = trend.split('&')[1].strip()
            listdata = eval(data)
            for d in listdata:
                # 如果存储，可以考虑只存储13位时间戳
                year_month = time.strftime("%Y-%m", time.localtime(d[0] / 1000))
                price = d[1]
                # csv模块写入数据到csv文件，文件第一行以self.header一致
                item['区域'] = district
                item['小区'] = lpname
                item['月份'] = year_month
                item['价格'] = price
                writer.writerow(item)
                if highest == {} or price>highest['price']:
                    highest['lpname'] = lpname
                    highest['year_month'] = year_month
                    highest['price'] = price
        print(highest)
        f.close()
        csvfile.close()
    except Exception as ex:
        print(ex)

# dir = r'E:\xsq\test\PycharmProjects\scrapy-FangTX\FangTX\sources\data-2018-04-19.json'
dir = r'E:\xsq\test\PycharmProjects\scrapy-FangTX\FangTX\analysis\f.json'
# read_json_file_1(dir.replace('\\','/'))
read_json_file_2(dir.replace('\\', '/'))

# f1= r'E:\xsq\test\PycharmProjects\scrapy-FangTX\FangTX\analysis\f1.json'
# f2= r'E:\xsq\test\PycharmProjects\scrapy-FangTX\FangTX\analysis\f2.json'