import requests
import json

with requests.Session() as session:
    login_url = "http://router.asus.com/login.cgi"
    
    login_data = {
        'action_wait': '5',
        'current_page': 'Main_Login.asp',
        'next_page': 'index.asp',
        'login_authorization': 'S0VSVDpwYXNzd29yZDEyMw=='
    }
    
    login_headers = {
        'Referer':'http://router.asus.com/Main_Login.asp',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    }
   
    login_res = session.post(login_url, headers=login_headers, data=login_data)
    url = "http://router.asus.com/ajax_onboarding.asp"
    headers = {
        'Referer':'http://router.asus.com/index.asp',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
    }
    
    res = session.get(url, headers=headers)
    res_text = res.text
    res_text = res_text[res_text.rfind('get_allclientlist'):-36].replace('get_allclientlist = ', '')
    res_json = json.loads(res_text)[0]['B0:6E:BF:66:07:80']
    
mac_2G = list(res_json['2G'].keys())
mac_5G = list(res_json['5G'].keys())

print(mac_2G)
print(mac_5G)