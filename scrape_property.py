import requests 
import json
import os
import csv

def read_file(file_name: str) -> str:
    with open(file_name, 'r') as f: return f.read()

def write_file(file_name: str, content: str) -> str:
    with open(file_name, 'w') as f: 
        f.write(content)
        return content

def download_json(file_name: str, url: str) -> object:
    if os.path.isfile(file_name):
        print(f'Already downloaded: {url}')
        return json.loads(read_file(file_name))
    else:
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        response = requests.get(url, headers={'Accept': 'application/json'}).text
        try:
            data = json.loads(response)
            write_file(file_name, response)
        except:
            data = { 'props' : { 'currentPage': 0, 'totalPages': -1, 'listingsMap': {} } }
            write_file(file_name, json.dumps(data))
        print(f'Successfully downloaded: {url}')
        return data

def download_listings(suburb: str, property_type: str, bedrooms: str, page: int = 1):
    url = f'https://www.domain.com.au/sold-listings/{suburb}/{property_type}/{bedrooms}/?excludepricewithheld=1&ssubs=0&page={page}'
    
    dir = f'data/20210723/{suburb}/{property_type}/{bedrooms}'
    os.makedirs(dir, exist_ok=True)

    page_number = str(page).zfill(3)
    file_name = f'{dir}/{page_number}.json'
    
    response = download_json(file_name, url)['props']

    current_page = response['currentPage']
    totalPages = response['totalPages']

    if current_page < totalPages:
        download_listings(suburb, property_type, bedrooms, current_page + 1)

with open ('./suburbs/brisbane-city-qld-4000-1.csv', newline='') as f:
    reader = csv.reader(f)
    suburbs = list(reader)

for suburb in suburbs:
    for property_type in ['apartment', 'house']:
        for bedrooms in ['1-bedroom', '2-bedrooms', '3-bedrooms', '4-bedrooms', '5-bedrooms']:
            download_listings(suburb[0], property_type, bedrooms)
        if property_type == 'apartment':
            download_listings(suburb[0], property_type, 'studio')
        if property_type == 'house':
            download_listings(suburb[0], property_type, '6-bedrooms')
        if property_type == 'house':
            download_listings(suburb[0], property_type, '7-bedrooms')
