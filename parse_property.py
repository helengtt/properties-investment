from glob import glob 
import json
import re
import datetime

def read_json_file(file_name: str) -> str:
    with open(file_name, 'r') as f: 
        return json.loads(f.read())

with open('properties.csv', 'w') as f:
    header =('{listing_id},{suburb},{property_type},{is_rural},{price},{beds},{baths},{parking},{land_size},{address_lat},{address_lng},{sold_channel},{sold_date},"{address_street}"\n'
            .replace('{', '')
            .replace('}', '')
            .replace('"', '')
    )
    f.write(header)
    for json_file in glob('data/20210723/*/*/*/*.json'):
        suburb = json_file.split('/')[2]
        properties = read_json_file(json_file)['props']['listingsMap']
        for listing_id, listing_payload in properties.items():
            model = listing_payload['listingModel']
            price = int(''.join(re.findall(r'\d', model['price'])))
            address = model['address']
            address_street = address.get('street').replace('\r\n', ' ') or ''
            address_lat = address.get('lat') or ''
            address_lng = address.get('lng') or ''
            features = model['features'] or ''
            beds = features.get('beds') or ''
            baths = features.get('baths') or ''
            parking = features.get('parking') or ''
            property_type = features.get('propertyType') or ''
            is_rural = features.get('isRural') or ''
            land_size = features.get('landSize') or ''
            land_unit = features.get('landUnit') or ''
            is_retirement = features.get('isRetirement') or ''
            tags=model['tags']['tagText'] or ''
            if tags:
                if 'private treaty' in tags:
                    sold_channel = 'private treaty'
                elif 'auction' in tags:
                    sold_channel = 'auction'
                else:
                    sold_channel = ''
                date_string = ' '.join(tags.split(' ')[-3:])
                try:
                    sold_date = datetime.datetime.strptime(date_string, "%d %b %Y").date()
                except:
                    sold_date = ''
            else:
                sold_channel = ''
                sold_date = ''
            print(f'{listing_id},{suburb},{property_type},{is_rural},{price},{beds},{baths},{parking},{land_size},{address_lat},{address_lng},{sold_channel},{sold_date},"{address_street}"')
            f.write(f'{listing_id},{suburb},{property_type},{is_rural},{price},{beds},{baths},{parking},{land_size},{address_lat},{address_lng},{sold_channel},{sold_date},"{address_street}"\n')

