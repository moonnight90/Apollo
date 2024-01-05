from requests import Session
from time import time
ses = Session()

headers = {
    'authority': 'app.apollo.io',
    'accept': '*/*',
    'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://app.apollo.io',
    'referer': 'https://app.apollo.io/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
}


ses.headers.update(headers)
json_data = {
    'email': 'richard@toplineemail.com',
    'password': 'GEoa&R3',
    'timezone_offset': -300,
    'cacheKey': int(time()*1000),
                
}

response = ses.post('https://app.apollo.io/api/v1/auth/login', headers=headers, json=json_data)
print(response.status_code)
print(response.text)
print(response.cookies.get_dict())