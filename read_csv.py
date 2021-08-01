import pandas as pd
from pandasql import sqldf
from pyspark import SparkContext as sc

# df = pd.read_csv('./data/properties.csv')
# print(df.head(200)) # failed

# read csv --------------------------------------------

# for df in pd.read_csv('./data/properties.csv', chunksize=20000, error_bad_lines=False):
#     # print(len(df))
#     # print(df.to_dict('records')[-1])
#     df.to_csv('./data/properties_read.csv', header=False, index=False, mode='a') #append

df = pd.read_csv('./data/properties_read.csv')
# print(df.head(200))

# grain check: -----------------------------------------

# result = sqldf('''
# --begin-sql
# SELECT COUNT(listing_id)
#         , COUNT(DISTINCT listing_id)
# FROM df
# --end-sql
# ''')
# #----- output: 0             681497                      672351

# # ------ check which grains are duplicated ------
# result = sqldf('''
# --begin-sql
# SELECT listing_id
#     , COUNT(listing_id) AS cnt
# FROM df
# GROUP BY listing_id
# ORDER BY cnt DESC
# --end-sql
# ''')

# # ------ check grains with distinct listing_id and output ------
# result = sqldf('''
# --begin-sql
# WITH properties_row_number AS (
# SELECT *
#     , COUNT(listing_id) AS cnt
#     , ROW_NUMBER() OVER (PARTITION BY listing_id) as rn
# FROM df
# GROUP BY listing_id
# ORDER BY cnt DESC
# )
# SELECT *
# --SELECT COUNT(listing_id)
# --    , COUNT(DISTINCT listing_id)
# FROM properties_row_number
# WHERE rn=1 AND property_type IN ('House', 'ApartmentUnitFlat')
# --GROUP BY listing_id
# --end-sql
# ''')

# # ------ check property_type only in house and apartment ------
# df2 = pd.read_csv('./data/properties_cleaned.csv')
# result = sqldf('''
# --begin-sql
# WITH properties_row_number AS (
# SELECT *
#     , COUNT(listing_id) AS cnt
#     , ROW_NUMBER() OVER (PARTITION BY listing_id) as rn
# --FROM df
# FROM df2
# GROUP BY listing_id
# ORDER BY cnt DESC
# )
# SELECT property_type
#     , COUNT(property_type)
#     , COUNT(DISTINCT property_type)
# FROM properties_row_number
# WHERE rn=1
# GROUP BY property_type
# --end-sql
# ''')

# output --------------------------------------------------------------

# print(result.head(200))
# #----- output:  0             672350                      672350

result.to_csv('./data/properties_cleaned.csv', columns='rn,listing_id,suburb,property_type,is_rural,price,beds,baths,parking,land_size,address_lat,address_lng,sold_channel,sold_date,address_street'.split(','))