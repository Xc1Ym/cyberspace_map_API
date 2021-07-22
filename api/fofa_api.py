# -*- coding: utf-8 -*-
# author: Xc1Ym
# github: https://github.com/Xc1Ym/FofaAPI
# If you have any problems, please give feedback to https://github.com/Xc1Ym/FofaAPI/issues
import requests
import json
import argparse
import base64
from prettytable import PrettyTable

'''
该fofa_API利用官方API实现，根据Fofa会员等级返回查询信息
同时还可以查询部分Fofa基础信息


请输入API身份认证参数，email为登录邮箱，key为个人资料中的API key
'''

email = ""
key = ""

class fofa:

    # 获取基础信息
    @staticmethod
    def Get_me(email_get_api, key_get_api):
        api = "https://fofa.so/api/v1/info/my?email={}&key={}".format(email_get_api, key_get_api)
        r_json = json.loads(requests.get(api).text)
        return r_json

    # 格式化基础信息
    @staticmethod
    def Get_information(r):
        print("当前用户昵称：" + r['username'])
        print("当前用户头像：" + r['avatar'])
        print("当前用户邮箱：" + r['email'])
        print("Fofa版本：" + r['fofacli_ver'])

    # 搜索功能
    def Get_search(self, email_get_api, key_get_api, search, size, page):
        # 请求FofaAPI
        qbase64 = base64.b64encode(search.encode())
        api = "https://fofa.so/api/v1/search/all?email={}&key={}&qbase64={}&page={}&size={}".format(email_get_api, key_get_api, qbase64.decode(), page, size)
        r = requests.get(api)
        r_json = json.loads(r.text)
        # print(r_json) # 服务端原生错误信息
        # 判断错误信息
        if r_json['error']:
            if r_json['errmsg'] == "Internal Server Error!":
                print("服务器错误")
            elif r_json['errmsg'] == "FOFA coin is not enough!":
                print("Fofa币不足")
            elif r_json['errmsg'] == "Result window is too large, page must be less than or equal to...!":
                print("结果窗口过大")
            elif r_json['errmsg'] == "limits must less than 10001":
                print("超过API限制")
            elif r_json['errmsg'] == "401 Unauthorized, make sure email and apikey is correct.":
                print("鉴权失败，请重新确认邮箱和API KEY")
            elif r_json['errmsg'] == '820103':
                print("格式错误，请重新输入")
        else:
            self.Print_search(r_json, size)

    # 格式化输出
    @staticmethod
    def Print_search(r_json, size):
        print("\n")
        print("页码：第{}页  数量：{}个".format(r_json['page'], r_json['size']))
        print("当前显示：{}个".format(size))
        print("查询内容：{}\n".format(r_json['query']))
        len_size = len(r_json['results'])
        r_list = r_json['results']
        table = PrettyTable(['序号', '地址', 'IP', '端口'])  # 绘制表格
        # 判断数量和显示
        intsize = int(size)
        if intsize <= len_size:
            for i in range(intsize):
                table.add_row([i + 1, r_list[i][0], r_list[i][1], r_list[i][2]])
        else:
            for i in range(len_size):
                table.add_row([i + 1, r_list[i][0], r_list[i][1], r_list[i][2]])
        print(table)

    # 版权信息
    def Copyright(self):
        bn = """
                 ______     __               _____ _____ 
                |  ____|   / _|        /\   |  __ \_   _|
                | |__ ___ | |_ __ _   /  \  | |__) || |  
                |  __/ _ \|  _/ _` | / /\ \ |  ___/ | |  
                | | | (_) | || (_| |/ ____ \| |    _| |_ 
                |_|  \___/|_| \__,_/_/    \_\_|   |_____|  
            --------------------------------------------- 
            author: Xc1Ym
            github: https://github.com/Xc1Ym/FofaAPI
            """
        print(bn)
        self.Terminal()

    # 命令行模块
    def Terminal(self):
        parser = argparse.ArgumentParser(description="e.g：python fofa_api.py --search IP or domain\t python fofa_api.py --search \"domain=xx.com\" or \"city=Beijing\"", prog="fofa_api.py")
        group = parser.add_mutually_exclusive_group()
        group.add_argument("--version", "-V", help="Show version of Fofa_API", action='version', version="| %(prog)s v1.2 |")
        group.add_argument("--search", "-S", help="Search key word", type=str)
        group.add_argument("--rule", help="Query fofa syntax rules", action="store_true")
        parser.add_argument("--size", help="Show the number of results.(default=100)", default=100)
        parser.add_argument("--page", help="Show the page of results.(default=1)", default=1)
        # parser.add_argument('word_search', help="search key word")
        args = parser.parse_args()
        if args.search:
            self.Get_search(email, key, args.search, args.size, args.page)
        else:
            if args.rule:
                self.Rule()

    # 高级查询语句模块
    @staticmethod
    def Rule():
        dict = {0:["title=beijing","从标题中搜索北京"],
                1:["header=elastic", "从http头中搜索elastic"],
                2:["body=网络空间测绘", "从html正文中搜搜网络空间测绘"],
                3:["domain=qq.com", "搜索根域名带有qq.com的网站"],
                4:["icp=京ICP证030173号", "查找备案号为京ICP证030173号的网站"],
                5:["js_name=js/jquery.js", "查找网站正文中包含js/jquery.js的资产"],
                6:["js_md5=82ac3f14327a8b7ba49baa208d4eaa15", "查找js源码与之匹配的资产"],
                7:["icon_hash=-247388890", "搜索使用此icon的资产"],
                8:["port=6379", "查找开发6379端口的资产"],
                9:["ip=1.1.1.1", "查找IP为1.1.1.1的资产"],
                10:["ip=1.1.1.1/24", "查找IP为1.1.1.1-1.1.1.255整个C段地址"],
                11:["status_code=402", "查找服务器状态为402的资产"],
                12:["protocol=quic", "查询quic协议资产"],
                13:["country=CN", "搜索指定国家(编码)的资产"],
                14:["region=Xinjiang", "搜索指定行政区的资产"],
                15:["city=Ürümqi", "搜索指定城市的资产"],
                16:["cert=baidu", "搜索证书(https或者imaps等)中带有baidu的资产"],
                17:["cert.subject=Oracle Corporation", "搜索证书持有者是Oracle Corporation的资产"],
                18:["cert.issuer=DigiCert", "搜索证书颁发者为DigiCert Inc的资产"],
                19:["cert.is_valid=true", "验证证书是否有效，true有效，false无效"],
                20:["banner=users && protocol=ftp","搜索FTP协议中带有users文本的资产"],
                21:["type=service", "搜索所有协议资产，支持subdomain和service两种"],
                22:["os=centos", "搜索CentOS资产"],
                23:["server==Microsoft-IIS/10", "搜索IIS 10服务器"],
                24:["app=Microsoft-Exchange", "搜索Microsoft-Exchange设备"],
                25:["after=\"2017\" && before=\"2017-10-01\"", "指定时间范围段搜索"],
                26:["asn=19551", "搜索指定ASN资产"],
                27:["org=Amazon.com, Inc.", "搜索指定组织的资产"],
                28:["base_protocol=udp", "搜索指定udp协议的资产"],
                29:["is_fraud=false", "排除仿冒/欺诈数据"],
                30:["is_honeypot=false", "排除蜜罐数据"],
                31:["is_ipv6=true", "搜索ipv6的资产"],
                32:["is_domain=true","搜索域名的资产"],
                33:["port_size=6", "查询开放端口数量等于6的资产"],
                34:["port_size_gt=6", "查询开放端口数量大于6的资产"],
                35:["port_size_lt=12", "查询开放端口数量小于12的资产"],
                36:["ip_ports=80,161", "搜索同时开放80和161端口的ip"],
                37:["ip_country=CN", "搜索中国的ip资产"],
                38:["ip_region=Zhejiang", "搜索指定行政区的ip资产"],
                39:["ip_city=Hangzhou", "搜索指定城市的ip资产"],
                40:["ip_after=\"2021-03-18\"", "搜索2021-03-18以后的ip资产"],
                41:["ip_before=\"2019-09-09\"", "搜索2019-09-09以前的ip资产"]
                }
        table = PrettyTable(['序号', '高级语法', '说明'])
        for i in range(len(dict)):
            table.add_row([i + 1, dict[i][0], dict[i][1]])
        print(table)