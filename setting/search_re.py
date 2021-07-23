import re

class Re:
    @staticmethod
    def regular(search):
        pattern = re.compile('((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
        search_ip = pattern.search(search)
        print(search_ip.group())
