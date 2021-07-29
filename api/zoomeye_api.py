from zoomeye.sdk import ZoomEye

class Zoom_eye:

    # 验证API KEY
    @staticmethod
    def zoomeye_key(api_key,search):
        zm = ZoomEye(api_key=api_key)
        #print(zm)
        Zoom_eye.zoom_search(zm, search)

    # 搜索模块
    @staticmethod
    def zoom_search(zm, zm_search):
        data = zm_search.dork_search('typecho')
        data2 = zm.get_facet()
        # print(data2)
        data1 = zm.dork_filter("ip,port")
        print(data1)