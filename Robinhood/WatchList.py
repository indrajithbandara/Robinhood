import json

class WatchList:
	def __init__(self,name=None,url=None,trader=None,to_create = False):
		assert trader is not None
		assert (name or url) is not None
		self.url = url
		self.name = name
		self.trader = trader
		if to_create:
			assert name is not None
			self.trader.session.post(
				'https://api.robinhood.com/watchlists/',
				data = {"name":name}
				)
		if url is None:
			self.url = 'https://api.robinhood.com/watchlists/{}/'.format(name)
	def add(self,*scodes):
		assert len(scodes)>0
		while len(scodes)>8:
			scodes_x = scodes[:8]
			scodes = scodes[8:]
			query = ','.join(scodes_x)
			self.trader.session.post(self.url,data = {"symbols":query})
	def get_price(self):
		data = self.trader.session.get(self.url).json()['results']
		keys = [self.trader.session.get(et['instrument']).json()['symbol'] for et in data]
		values = [float(self.trader.last_trade_price(scode)[0][0]) for scode in keys]
		return dict(zip(keys,values))
	def get_symbols(self):
		data = self.trader.session.get(self.url).json()['results']
		return keys = [self.trader.session.get(et['instrument']).json()['symbol'] for et in data]

