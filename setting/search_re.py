import re

class Re:
    @staticmethod
    def regular(search):
        re_ip = re.compile('((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')# 匹配IP
        re_domain = re.compile('[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?')# 匹配域名

        search_domain = re_domain.search(search)
        if not search_domain is None:
            search_ip = re_ip.search(search)
            print(search_domain)
            print(1)
            if not search_ip is None:
                print(search_ip)
                print(2)
            else:
                print(3)
        else:
            print(4)