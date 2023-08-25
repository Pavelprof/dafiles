import os
from tinkoff.invest import Client, InstrumentIdType

TOKEN = os.environ["TIN_API_KEY"]
#
# def get_prices_by_figi(figi_list):
#     with Client(TOKEN) as client:
#         r = client.market_data.get_market_search_by_figi(figi=figi_list)
#         prices = {}
#         for item in r.payload.instruments:
#             if item.figi in figi_list:
#                 prices[item.figi] = item.last_price
#
#         return prices
#


# figi by ticker and class_code
with Client(TOKEN) as client:
    res = client.instruments.currency_by(
        id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_TICKER,
        class_code='CETS',
        id = 'USD000UTSTOM'
    )

    # res = client.instruments.etf_by(
    #     id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_TICKER,
    #     class_code='CETS',
    #     id = 'USD000UTSTOM')
    print(res)


# last price by figi
# with Client(TOKEN) as client:
#     r = client.market_data.get_last_prices(figi=['BBG0120X0XX2','BBG004731032','BBG004S68B31',])
#     print(r)
#     print(type(r))
#     print(r.last_prices[0])
#     print(type(r.last_prices[0]))
#     print(r.last_prices[0].price)
#     print(type(r.last_prices[0].price))
#     p = r.last_prices[0].price
#     price = p.units + p.nano / 1e9
#     print(price)
