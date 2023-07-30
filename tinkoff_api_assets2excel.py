import os
import pandas as pd
from tinkoff.invest import Client

TOKEN = os.environ["TIN_API_KEY"]

with Client(TOKEN) as client:
    ass = client.instruments.get_assets()

    data = []

    for asset in ass.assets:
        instrument = asset.instruments[0] if asset.instruments else None
        data.append([
            asset.uid,
            asset.type,
            asset.name,
            instrument.figi if instrument else "",
            instrument.instrument_type if instrument else "",
            instrument.ticker if instrument else "",
            instrument.class_code if instrument else "",
            instrument.instrument_kind.name if instrument else "",
        ])

    columns = ["UID", "Type", "Name", "FIGI", "Instrument Type", "Ticker", "Class Code", "Instrument Kind"]
    df = pd.DataFrame(data, columns=columns)

    df.to_excel("tinkoff_instruments.xlsx", index=False)

print("Data saved to tinkoff_instruments.xlsx")
