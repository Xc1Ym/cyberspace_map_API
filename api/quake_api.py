import requests
import json
from prettytable import PrettyTable


class Quake_360:

    # 搜索模块
    def Search(self, key, search, size, page):
        headers = {"X-QuakeToken": key}

        data = {
            "query": search,
            "start": page,
            "size": size
        }
        response = requests.post(url="https://quake.360.cn/api/v3/search/quake_service", headers=headers, json=data)
        r_json = json.loads(response.text)
        # print(r_json)
        self.Print_search(r_json, search)

    def Print_search(self, r_json, search):
        print("\n")
        print("页码：第{}页  共{}页  总数量：{}个".format(r_json['meta']['pagination']['page_index'],
                                              r_json['meta']['pagination']['page_size'],
                                              r_json['meta']['pagination']['total']))
        print("查询内容：{}".format(search))
        len_size = len(r_json['data'])
        table = PrettyTable(['序号', '地址', 'IP', '端口'])  # 绘制表格
        for i in range(len_size):
            table.add_row([i + 1, r_json['data'][i]['service']['http']['host'], r_json['data'][i]['ip'],
                           r_json['data'][i]['port']])
        print(table)