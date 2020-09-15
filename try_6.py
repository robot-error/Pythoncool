import requests
import sys
import json,pyexcel_xls
import os
import time

class Logger(object):

    def __init__(self, filename='default.log', stream=sys.stdout):
        self.terminal = stream

        self.log = open(filename, 'w')

    def write(self, message):
        self.terminal.write(message)

        self.log.write(message)

    def flush(self):
        pass

sys.stdout = Logger('a.log', sys.stdout)
sys.stderr = Logger('a.log_file', sys.stderr)

def get_data():
    """
    获取高德数据
    """
    url = "https://restapi.amap.com/v3/traffic/status/rectangle?key=dc2065ba05fee31d8df32d47f5b586f7&rectangle={address}"

    #列表存储坐标对
    address = ["117.032086, 36.667018;117.072905, 36.689247",
               " 117.052200, 36.697200; 117.10300, 36.719300"]
    #字典储存返回信息
    total = {
        'extensions': 'all',
    }
    r = requests.get(url=url.format(address=address), params=total)

def main():
    # url
    url = "https://restapi.amap.com/v3/traffic/status/rectangle?key=dc2065ba05fee31d8df32d47f5b586f7&rectangle={address}"

    # 坐标列表 想改变爬取路更改坐标地址即可限制范围在
    addresses = ["117.032086, 36.667018;117.072905, 36.689247",
                 " 117.052200, 36.697200; 117.10300, 36.719300"]

    pa = {
        'level': 6,
        'extensions': 'all',
    }

    i = 1
    while i <= 1:
        for address in addresses:
            r = requests.get(url=url.format(address=address), params=pa)
            i += 1
            json_data = json.loads(r.text)  # 转码
            text = eval(r.text)  # 将json格式转换为字典格式
            print(text)

        excel_totallist = [["name", "status", "direction", "angle","speed", "lcodes","polyline"]]
        excel_dic = {"timi": excel_totallist}

        # 遍历原来的字典的数据结构
        for item in text["trafficinfo"]["roads"]:
            try:
                name = item["name"]
            except:
                name = None
            try:
                status = item["status"]
            except:
                status = None
            try:
                direction = item["direction"]
            except:
                direction = None
            try:
                angle = item["angle"]
            except:
                angle = None
            try:
                speed = item["speed"]
            except:
                speed = None
            try:
                lcodes = item["lcodes"]
            except:
                lcodes = None
            try:
                polyline = item["polyline"]
            except:
                polyline = None

            itemlist = [name, status, direction, angle, speed, lcodes,polyline]

            excel_totallist.append(itemlist)
            time.strftime("%H:%M:%S")
        abspath = os.path.join("t1.xls")
        pyexcel_xls.save_data(abspath, excel_dic)

if __name__ == '__main__':
    main()
