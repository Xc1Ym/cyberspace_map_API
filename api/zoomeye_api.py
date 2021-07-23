from zoomeye.sdk import ZoomEye

class Zoom_eye:

    # 验证API KEY
    @staticmethod
    def zoomeye_key():
        zm = ZoomEye(api_key="17AFC5E8-132b-43b7d-8e1b-3ea963bfea7")
        #print(zm)
        return zm

    # 搜索模块
    @staticmethod
    def zoom_search(zm_search):
        data = zm_search.dork_search('typecho')
        data2 = zm.get_facet()
        # print(data2)
        data1 = zm.dork_filter("ip,port")
        print(data1)

if __name__ == '__main__':
    zm = Zoom_eye.zoomeye_key()
    Zoom_eye.zoom_search(zm)