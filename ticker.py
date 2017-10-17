import requests
from time import sleep

def bitstamp_price(pair):
	url = "https://www.bitstamp.net/api/v2/ticker/"+pair
	data = requests.get(url).json()
	return float(data['last'])

def kraken_price(pair):
	url = 'https://api.kraken.com/0/public/Ticker?pair='+pair
	data = requests.get(url).json()
	return float(data['result']['XXBTZEUR']['c'][0])

def bitfinex_price(pair):
	url = 'https://api.bitfinex.com/v2/tickers?symbols=t'+pair.upper()
	data = requests.get(url).json()
	return float(data[0][7])


while True:
	bitstamp = bitstamp_price("btceur")
	kraken = kraken_price("xbteur")
	bitfinex = bitfinex_price('btceur')
	print("Bitstamp: {0}\nKraken: {1}\nBitfinex: {2}\n".format(bitstamp,kraken,bitfinex))
	sleep(10)
