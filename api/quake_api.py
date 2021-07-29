import requests
import json


class Quake_360:
    @staticmethod
    def search(key, search, size, page):
        headers = {"X-QuakeToken": key}

        data = {
            "query": search,
            "start": page,
            "size": 1
        }
        response = requests.post(url="https://quake.360.cn/api/v3/search/quake_service", headers=headers, json=data)
        r_json = json.loads(response.text)
        print(r_json)