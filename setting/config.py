import json

def config():
    with open("./setting/config.json", encoding='utf-8') as f:
        json_api = json.loads(f.read())
        fofa_email = json_api['fofa_email']
        fofa_key = json_api['fofa_key']
        zoomeye_key = json_api['zoomeye_key']
        shodan_key = json_api['shodan_key']
        return fofa_email, fofa_key, zoomeye_key, shodan_key