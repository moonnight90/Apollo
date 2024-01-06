import os
from requests import Session
from time import time
import getpass
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

client.headers.update(main_headers) 

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

def get_lists(search_for):
    
    request_payload = {"label_modality":search_for,"page":1,"display_mode":"explorer_mode","per_page":50,"open_factor_names":[],"num_fetch_result":2,"show_suggestions":False,"ui_finder_random_seed":"xycezf0nren","cacheKey":int(time()*1000)}
    saved_lists = []
    while True:
        response = client.post(BASE_URL+"labels/search",json=request_payload)
        json_res = response.json()
        for label in json_res['labels']:
            saved_lists.append(label)
            print(f"{len(saved_lists)}: "+label['name'])
        if request_payload['page']>= json_res['pagination']['total_pages']:break
        request_payload['page'] +=1
    if len(saved_lists):
        return saved_lists[int(input('[?] Enter Choice: '))-1]['id']
    else: return False

def parse_for_companies(accounts): return [{
        "Name":account.get('name',None),
        "City":account.get('organization_city',None),
        "Country":account.get('organization_country',None),
        "Postal_code":account.get('organization_postal_code',None),
        "State":account.get('organization_state',None),
        "Street_address":account.get('organization_street_address',None),
        'Phone':account.get('phone',None),
        'Founded_year': account.get('founded_year',None),
        "Facebook":account.get('facebook_url',None),
        "Linkedin": account.get('linkedin_url',None),
        "Twitter": account.get('twitter_url',None),
        "Blog": account.get('blog_url',None),
        "Crunchbase": account.get('crunchbase_url',None),
        "Website": account.get('website_url',None)} for account in accounts]

def parse_for_people(accounts): return [{
    "First_name":account.get('first_name',None),
    "Last_name": account.get('last_name',None),
    "Full_name": account.get('name',None),
    "Title": account.get('title',None),
    "Email": account.get('email',None),
    "Linkedin": account.get('linkedin_url',None),
    "City": account.get('city',None),
    "State": account.get('state',None),
    "Country": account.get('country',None),
    "Phone": account.get('sanitized_phone',None),
    
    "Company_name": account.get('account',{}).get('name',None),
    "Company_phone": account.get('account',{}).get('phone',None),
    "Company_founded_year": account.get('account',{}).get('founded_year',None),
    "Company_website": account.get('account',{}).get('website_url',None),
    "Company_twitter": account.get('account',{}).get('twitter_url',None),
    "Company_linkedin": account.get('account',{}).get('linkedin_url',None),
    "Company_blog": account.get('account',{}).get('blog_url',None),
    "Company_crunchbase": account.get('account',{}).get('crunchbase_url',None),

    } for account in accounts]


def scrape_list(id):
    sear_for = "companies" if com_peop=='c' else 'people'
    request_payload = {"%s_label_ids"%search_for.removesuffix('s'):[id],"prospected_by_current_team":["yes"],"page":1,"display_mode":"explorer_mode","per_page":25,"open_factor_names":[],"num_fetch_result":1,"context":"%s-index-page"%sear_for,"show_suggestions":False,"ui_finder_random_seed":"okomp050hmr","cacheKey":int(time()*1000)}
    companies_list = []
    while True:
        response = client.post(BASE_URL+"mixed_%s/search"%sear_for,json=request_payload)
        json_res = response.json()
        companies_list.extend(parse_for_companies(json_res['accounts']) if com_peop=='c' else parse_for_people(json_res['contacts']))
        print(f"[!] {len(companies_list)}/{json_res['pagination']['total_entries']}")
        if request_payload['page'] >=json_res['pagination']['total_pages']: break
        request_payload['page'] +=1
    return companies_list

save_file = lambda results,filepath : pd.DataFrame(results).to_csv(filepath,index=False,mode='a',header=not os.path.exists(filepath))

if __name__ == "__main__":
    email = input('[?] Email: ')
    password = getpass.getpass(prompt='[?] Password: ')
    
    if login(email,password):
        while True:
            com_peop = input("[?] People/Companies?(P?C): ").lower()
            if com_peop=='c': search_for = "accounts";break
            elif com_peop == 'p': search_for = 'contacts';break
            else: input('[!] Invalid Input! Retry')

        while True:
            id = get_lists(search_for=search_for)
            if id:
                results = scrape_list(id)
                save_file(results,"companies_data.csv" if com_peop=='c' else "people_data.csv")
                if input('[?] Do you wanna scrape more (Y?N): ').lower()=='n':break
            else:
                print("[!] No List Found...")
                break


#companies "accounts"
#people    "contacts"