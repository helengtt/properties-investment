import pandas as pd 
from pandasql import sqldf
from haversine import haversine
from operator import itemgetter

with open('./suburbs/adelaide-sa-5000.csv', 'w') as f:
    f.write('home_suburb,near_by_suburb,postcode,distance\n')

    input = pd.read_csv('suburbs.csv')

    data = list(input.to_dict('records'))

    def coordinates(suburb: dict) -> tuple:
        return (suburb['lat'], suburb['lng'])

    centre = next(obj for obj in data if obj['suburb_id'] == 'adelaide-sa-5000')
    centre_name = centre['suburb_id']
    suburbs = [obj for obj in data if 5000 <= obj['postcode'] <= 5040]

    result = [(suburb['suburb_id'], suburb['postcode'], haversine(coordinates(suburb), coordinates(centre))) for suburb in suburbs]
    result = sorted(result, key=itemgetter(1,2))
    for suburb in result:
        name = suburb[0]
        postcode = suburb[1]
        distance = suburb[2]
        csv = f'"{centre_name}","{name}","{postcode}",{distance}\n'
        f.write(csv)
        # print(csv)

# print(len(result))
