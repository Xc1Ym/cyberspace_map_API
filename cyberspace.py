from api import fofa_api
from api.zoomeye_api import Zoom_eye
from setting import copyright, config, usage, search_re
from api import quake_api

if __name__ == '__main__':

    # 引入API KEY
    fofa_email, fofa_key, zoomeye_key, shodan_key, quake_key = config.config()
    # 引入版权信息
    copyright.CopyRight()
    # 引入命令行参数设置
    search, size, page = usage.Terminal()
    #print(search, szie, page)
    # 正则匹配以适应各API
    # search_re.Re().regular(search)
    '''
    if szie == -1 and page == -2:
        fofa_api.fofa().Rule()
    elif szie == -2 and page == -1:
        fofa_api.fofa().Get_information(fofa_email, fofa_key)
    else:
        fofa_api.fofa().Get_search(fofa_email, fofa_key, search, szie, page)
        '''
    # Zoom_eye.zoomeye_key(zoomeye_key, search)
    quake_api.Quake_360.Search(quake_key, search, size, page)
    # 三个任选
    #fofa_api.fofa().Terminal(fofa_email,fofa_key) # 调用Fofa API
    #shodan_api # 调用shodan API
     # 调用zoomeye API

