import requests
from datetime import datetime
import pandas as pd

# Pulls spread data from the Kraken public api for a given currency pair
# Formats the response more nicely and returns it as a dataframe
# Intended to be used in as a function in IPython but can be easily adapted into a standalone script

def kraken_spread(pair):
    df = requests.get('https://api.kraken.com/0/public/Spread?pair={}'.format(pair)).json()['result']
    df = df[list(df.keys())[0]]
    df = pd.DataFrame(df,columns=['time','bid','ask'])
    df['bid'] = df['bid'].apply(lambda x: float(x))
    df['ask'] = df['ask'].apply(lambda x: float(x))
    df['time'] = df['time'].apply(lambda x: datetime.fromtimestamp(x))
    df['%'] = ((df['ask'] - df['bid'])/df['bid'])*100
    return df


print(kraken_spread('xbteur'))
