import os
from tinkoff.invest import Client, InstrumentIdType

TOKEN = os.environ["TIN_API_KEY"]

figi_list = ['BBG0120X0XX2']
# ['BBG0120X0XX2','BBG004731032','BBG000BKDWB5', 'BBG001Y2XS07']

# get last prices
def get_quotes_from_tinkoff(figi_list):
    with Client(TOKEN) as client:
        r = client.market_data.get_last_prices(figi=figi_list)
        tf_quote_objects = {price.figi: price for price in r.last_prices}
        tf_quotes = {k: v.price.units + v.price.nano * 1e-9 for k, v in tf_quote_objects.items()}
        return tf_quotes
print(get_quotes_from_tinkoff(figi_list))

# currency by figi
# with Client(TOKEN) as client:
#     res = client.instruments.get_instrument_by(
#         id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI,
#         id='BBG001Y2XS07')
#     isin = (res.instrument.currency)

# currency_figi by ticker and class_code
# with Client(TOKEN) as client:
#     res = client.instruments.currency_by(
#         id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_TICKER,
#         class_code='CETS',
#         id = 'USD000UTSTOM')
#     print(res)

# etf_figi by ticker and class_code
# with Client(TOKEN) as client:
#     res = client.instruments.etf_by(
#         id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_TICKER,
#         class_code='CETS',
#         id = 'USD000UTSTOM')
#     print(res)

# share_figi by ticker and class_code
# with Client(TOKEN) as client:
#     res = client.instruments.share_by(
#         id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_TICKER,
#         class_code='TQBR',
#         id = 'BSPBP')
#     print(res)

# last price by figi
# with Client(TOKEN) as client:
    # r = client.market_data.get_last_prices(figi_list)
    # print(r)
    # print(type(r))
    # print(r.last_prices[0])
    # print(type(r.last_prices[0]))
    # print(r.last_prices[0].price)
    # print(type(r.last_prices[0].price))
    # p = r.last_prices[0].price
    # price = p.units + p.nano / 1e9
    # print(price)
