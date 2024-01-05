from requests import Session
from time import time
import pandas as pd

client = Session() # http requests client

BASE_URL = "https://app.apollo.io/api/v1/"

main_headers = {
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

client.headers.update(main_headers) # 

def login(email,password):
    login_payload = {
    'email': email,
    'password': password,
    'timezone_offset': -300,
    'cacheKey': int(time()*1000)
    }
    
    response = client.post(BASE_URL+'auth/login', json=login_payload)
    if response.status_code == 401:
        print("[LOGIN FAILED]: "+response.json()['message'])
        return False
    elif response.status_code == 200:
        users = response.json()['bootstrapped_data']['users']
        if len(users):
            name = users[0]['name']
            print('[LOGIN SUCCESS]: WELCOME %s'%name)
        cookies = response.cookies.get_dict()
        response.headers.update({'X-CSRF-TOKEN':cookies['X-CSRF-TOKEN']})
        client.cookies.update(cookies)
        return True

def get_lists():
    
    request_payload = {"label_modality":"accounts","page":1,"team_lists_only":["no"],"display_mode":"explorer_mode","per_page":50,"open_factor_names":[],"num_fetch_result":2,"show_suggestions":False,"ui_finder_random_seed":"xycezf0nren","cacheKey":int(time()*1000)}
    saved_lists = []
    while True:
        response = client.post(BASE_URL+"labels/search",json=request_payload)
        json_res = response.json()
        for label in json_res['labels']:
            saved_lists.append(label)
            print(f"{len(saved_lists)}: "+label['name'])
        if request_payload['page']>= json_res['pagination']['total_pages']:break
        request_payload['page'] +=1
    return saved_lists[int(input('[?] Enter Choice: '))-1]['id']


def scrape_list(id):
    request_payload = {"account_label_ids":[id],"prospected_by_current_team":["yes"],"page":1,"display_mode":"explorer_mode","per_page":25,"open_factor_names":[],"num_fetch_result":1,"context":"companies-index-page","show_suggestions":False,"ui_finder_random_seed":"okomp050hmr","cacheKey":int(time()*1000)}
    companies_list = []
    while True:
        response = client.post(BASE_URL+"mixed_companies/search",json=request_payload)
        json_res = response.json()
        accounts = json_res['accounts']
        companies_list.extend([
            {
                "Name":account['name'],
                "City":account['organization_city'],
                "Country":account['organization_country'],
                "Postal_code":account['organization_postal_code'],
                "State":account['organization_state'],
                "Street_address":account['organization_street_address'],
                'Phone':account['phone'],
                'Founded_year': account['founded_year'],
                "Facebook":account['facebook_url'],
                "Linkedin": account['linkedin_url'],
                "Twitter": account['twitter_url'],
                "Blog": account['blog_url'],
                "Crunchbase": account['crunchbase_url'],
                "Website": account['website_url'],                
            } for account in accounts])
        if request_payload['page'] >=json_res['pagination']['total_pages']: break
        request_payload['page'] +=1
    return companies_list
    
if __name__ == "__main__":
    # hjw6sryf0gvdxws@colesac.info
    if login('hjw6sryf0gvdxws@colesac.info','(Pakistan99)'):
        if get_lists():
            