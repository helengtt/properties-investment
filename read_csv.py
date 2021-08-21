import pandas as pd
from pandasql import sqldf

# Step 1: read csv, failed ---------------------------------------

# df = pd.read_csv('./data/properties.csv')
# print(df.head(200))

# Step 2: read csv successully --------------------------------------------

# for df in pd.read_csv('./data/properties.csv', chunksize=20000, error_bad_lines=False):
#     # print(len(df))
#     # print(df.to_dict('records')[-1])
#     df.to_csv('./data/properties_read.csv', header=False, index=False, mode='a') #append

df = pd.read_csv('./data/properties_read.csv')
# print(df.head(200))

# Step 3: grain check: ----------------------------------------- 

# 3.1 grain check, duplicated grains exist -----------------------------

# result = sqldf('''
# --begin-sql
# SELECT COUNT(listing_id)
#         , COUNT(DISTINCT listing_id)
# FROM df
# --end-sql
# ''')
# print(result.head(200))
# #----- output: 0             681497                      672351

# 3.2 check which grains are duplicated --------------------------------

# result = sqldf('''
# --begin-sql
# SELECT listing_id
#     , COUNT(listing_id) AS cnt
# FROM df
# GROUP BY listing_id
# ORDER BY cnt DESC
# --end-sql
# ''')
# print(result.head(200))

# 3.3 filter grains with distinct listing_id, property_type only in house and apartment, price is over 200000 ----------------------------

result_filtered = sqldf('''
--begin-sql
WITH properties_row_number AS (
SELECT *
    , COUNT(listing_id) AS cnt
    , ROW_NUMBER() OVER (PARTITION BY listing_id) as rn
FROM df
GROUP BY listing_id
ORDER BY cnt DESC
)
SELECT *
FROM properties_row_number
WHERE rn=1 AND property_type IN ('House', 'ApartmentUnitFlat') AND price >= 200000
--end-sql
''')
# print(result_filtered.head(200))

# 3.4 check listing_id again ---------------------------------------

check_listing_id = sqldf('''
--begin-sql
SELECT COUNT(listing_id)
        , COUNT(DISTINCT listing_id)
FROM result_filtered
--end-sql
''')
# print(check_listing_id.head(200))
#----- output:  0             650469                      650469


# 3.5 check property_type again -------------------------------------------

# check_property_type = sqldf('''
# --begin-sql
# SELECT property_type
# FROM result_filtered
# GROUP BY property_type
# --end-sql
# ''')
# print(check_property_type.head(200))

result_filtered.to_csv('./data/properties_cleaned.csv', columns='rn,listing_id,suburb,property_type,is_rural,price,beds,baths,parking,land_size,address_lat,address_lng,sold_channel,sold_date,address_street'.split(','))