import requests

cookies = {
    'remember_token_leadgenie_v2': 'eyJfcmFpbHMiOnsibWVzc2FnZSI6IklqWTFPVFU1T1RBMVpXTmlabU5sTURNd01EZG1NV1JsTkY4eFl6ZGxNelJsWVRNeFltVXhOMk0yT1RVME1ERTNOREk0Tmpka1pqSXpNaUk9IiwiZXhwIjoiMjAyNC0wMi0wNFQwNDo1MjoxOS4xNTdaIiwicHVyIjoiY29va2llLnJlbWVtYmVyX3Rva2VuX2xlYWRnZW5pZV92MiJ9fQ%3D%3D--fba21d9de9620183fe20337fa7c681e11aabfba6',
    'X-CSRF-TOKEN': 'ZUOtBrTU8oTX0MLa7dWfTcER9GomHt30jj0vKTSsMponO0CsKL47ZUJojxvI27CsUwaW3tvuQ2uxzdMhGquxiQ',
}



json_data = {
    'finder_table_layout_id': None,
    'finder_view_id': '5a205be49a57e40c095e1d60',
    'account_label_ids': [
        '65959ad1fd28a501c69146cf',
    ],
    'prospected_by_current_team': [
        'yes',
    ],
    'page': 2,
    'display_mode': 'explorer_mode',
    'per_page': 25,
    'open_factor_names': [
        'prospected_by_current_team',
    ],
    'num_fetch_result': 3,
    'context': 'companies-index-page',
    'show_suggestions': False,
    'ui_finder_random_seed': 'mm8arxxmwaa',
    'cacheKey': 1704343981839,
}

response = requests.post('https://app.apollo.io/api/v1/mixed_companies/search', cookies=cookies, json=json_data)

print(response.text)
print(response.status_code)