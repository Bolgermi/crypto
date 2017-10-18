import requests
from time import sleep

# Pulls the last price from the relevant exchange for the currency pair or instrument in question

def bitstamp_price(pair):
	url = "https://www.bitstamp.net/api/v2/ticker/"+pair
	data = requests.get(url).json()
	return float(data['last'])

def kraken_price(pair):
	url = 'https://api.kraken.com/0/public/Ticker?pair='+pair
	data = requests.get(url).json()
	return float(data['result']['XXBTZEUR']['c'][0])

def bitmex_price(instrument):
	url = 'https://www.bitmex.com/api/v1/instrument?symbol={}&columns=lastPrice'.format(instrument.upper())
	data = requests.get(url).json()
	return float(data[0]['lastPrice'])

def poloniex_price(pair):
	url = "https://poloniex.com/public?command=returnTicker"
	data = requests.get(url).json()
	return float(data[pair.upper()]['last'])

while True:
	# Call functions for currencies or exchanges as needed here
	bitstamp = bitstamp_price("btceur")
	kraken = kraken_price("xbteur")
	print("Bitstamp: {0}\nKraken: {1}\n".format(bitstamp,kraken))
	sleep(10)
