import requests
import pandas as pd

def get_currency_info():
    open_exchange_url = 'https://openexchangerates.org/api/currencies.json'
    currencies_response = requests.get(open_exchange_url)
    currencies_data = currencies_response.json()

    rest_countries_url = 'https://restcountries.com/v3.1/all'
    countries_response = requests.get(rest_countries_url)
    countries_data = countries_response.json()

    currency_country_mapping = {}
    for country in countries_data:
        if 'currencies' in country:
            for code, currency_info in country['currencies'].items():
                country_code = country['cca2']
                name = currency_info['name']
                currency_country_mapping[code] = {
                    'country_code': country_code,
                    'name': name
                }

    final_currency_list = []
    for ticker, full_name in currencies_data.items():
        if ticker in currency_country_mapping:
            country_code = currency_country_mapping[ticker]['country_code']
            name = currency_country_mapping[ticker]['name']
        else:
            country_code = 'Unknown'
            name = 'Unknown'

        currency_info = {
            'ticker': ticker,
            'full_name_asset': full_name,
            'country_asset': country_code,
            'type_asset': 'CY',
            'is_tradable': True,
            'name_asset': name,
            'currency_influence': ticker,
            'type_base_asset': 'CY',
            'currency_base_settlement': ticker,
            'exchange': 4
        }
        final_currency_list.append(currency_info)
        currencies_info = final_currency_list

    return currencies_info


def save_to_excel(data):
    df = pd.DataFrame(data)

    excel_filename = r'C:\Users\Павел\Desktop\currencies_info.xlsx'
    df.to_excel(excel_filename, index=False)

currencies_info = get_currency_info()

save_to_excel(currencies_info)
