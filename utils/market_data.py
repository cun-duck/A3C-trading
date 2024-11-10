import requests
import pandas as pd

def get_market_data(api_key, symbol, interval='1h', start_date=None, end_date=None):
    url = f'https://api.twelvedata.com/time_series'
    params = {
        'symbol': symbol,
        'interval': interval,
        'apikey': api_key
    }
    if start_date:
        params['start_date'] = start_date
    if end_date:
        params['end_date'] = end_date

    response = requests.get(url, params=params)
    data = response.json()

    if 'values' in data:
        df = pd.DataFrame(data['values'])
        df['datetime'] = pd.to_datetime(df['datetime'])
        df.set_index('datetime', inplace=True)
        df = df.astype(float)
        return df
    else:
        print(f"Error fetching data: {data.get('message', 'Unknown error')}")
        return None
