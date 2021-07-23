import shodan
from prettytable import PrettyTable
import math

class shodan_api:
    API_key=""
    search = ''

    # 连接API
    def Get_api(self):
        api = shodan.Shodan(self.API_key)
        return api

    # 搜索功能
    def Get_search(self, api):
        try:
            # Search Shodan
            results = api.search(self.search)
            return results
        except shodan as e:
            print('Error: {}'.format(e))

    # 格式化输出
    def Print_search(self, results):
        print("\n")
        intsize = int(results['total'])
        page = math.ceil(intsize / 100)
        print("页码：{}  数量：{}".format(page, results['total']))
        print("当前显示：{}个".format(100))
        print("查询内容：{}\n".format(self.search))
        print(results)
        table = PrettyTable(['序号', '地址', 'IP'])#, '端口'])  # 绘制表格
        if intsize <= 100:
            for i in range(intsize):
                table.add_row([i + 1, results['matches'], results['matches']])

            print(table)

if __name__ == "__main__":
    Shodan = shodan_api()
    shodan_api = Shodan.Get_api()
    shodan_search = Shodan.Get_search(shodan_api)
    Shodan.Print_search(shodan_search)