# Data Science Project: Property Investment
## Project Introduction
The project aims to find out the target suburbs for potential investment opportunities in the residential property market of Australia’s biggest cities.

## To extract original property data:

This repo uses python to scrape property data from <a href = "domain.com.au" target="_blank">domain.com.au</a>.
Scraping codes: <a href="https://github.com/helengtt/properties-investment/blob/main/scrape_property.py" target="_blank">scrape_property.py</a>
Parsing codes: <a href="https://github.com/helengtt/properties-investment/blob/main/parse_property.py" target="_blank">parse_property.py</a>

This repo uses haversine formula to calculate the distances from suburbs to the cities seperately:
Sydney<a href="https://github.com/helengtt/properties-investment/blob/main/suburb_dis_syd.py" target="_blank">suburb_dis_syd.py</a>
Melbourne<a href="https://github.com/helengtt/properties-investment/blob/main/suburb_dis_mel.py" target="_blank">suburb_dis_mel.py</a> 
Brisbane<a href="https://github.com/helengtt/properties-investment/blob/main/suburb_dis_qld.py" target="_blank">suburb_dis_qld.py</a>
Perth<a href="https://github.com/helengtt/properties-investment/blob/main/suburb_dis_wa.py" target="_blank">suburb_dis_wa.py</a>
Adailaide<a href="https://github.com/helengtt/properties-investment/blob/main/suburb_dis_sa.py" target="_blank">suburb_dis_sa.py</a>

## To read, check and clean the property data:
We read the original data from scraping successfully, then did property grain check and null check to remove duplicated and invalid records, and cleaned the data step by steps.
<a href="https://github.com/helengtt/properties-investment/blob/main/read_check_clean_property.py" target="_blank">read_check_clean_property.py</a>

## To extract features and analyse
- Read data, Upload to PostgreSQL
- Extract features for dimension tables
    - Affordability in suburbs
    - Percentage among bedrooms
    - Median Price and Capital Growth
    - Median Price and monthly Growth
- Combine Suburb features
The data can be found in [domain.ipynb](https://github.com/helengtt/properties-investment/blob/main/ipynb/domain.ipynb)

## Reports
[aus_residential_property_investment_analytics_report.ipynb](https://github.com/helengtt/properties-investment/blob/main/ipynb/aus_residential_property_investment_analytics_report.ipynb)


