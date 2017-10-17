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


while True:
	bitstamp = bitstamp_price("btceur")
	kraken = kraken_price("xbteur")
	print("Bitstamp: {0}\nKraken: {1}\n".format(bitstamp,kraken))
	sleep(10)
