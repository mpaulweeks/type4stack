import urllib2
import json

class Demo():
	@staticmethod
	def demo():
		url = 'https://api.deckbrew.com/mtg/cards?oracle={G}&oracle={W}&type=land'
		json_data = urllib2.urlopen(url)
		data = json.load(json_data)
		cards = []
		for c in data:
			if c['name'].lower() == 'azorius chancery':
				cards.append(c)
		return cards