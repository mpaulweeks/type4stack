from type4.models import Card, Status
from operator import attrgetter
from collections import defaultdict

import logging
logger = logging.getLogger(__name__)

class CardWrapper():

	def was_in_stack(self, moment):
		for status in self.status_history:
			if status.timestamp < moment:
				return status.is_in_stack()
		return False
	
	def is_in_stack(self):
		return self.current_status.is_in_stack()

	def __init__(self, card, statuses):
		self.card = card
		self.name = card.name
		sorted_statuses = sorted(
			statuses, key=attrgetter('timestamp'), reverse=True)
		self.status_history = sorted_statuses
		self.current_status = sorted_statuses[0]

	@staticmethod
	def get_cards():	
		statuses = Status.objects.all()
		status_dict = defaultdict(list)
		for s in statuses:
			status_dict[s.card_id].append(s)
		cards = Card.objects.all()
		wrappers = []
		for c in cards:
			wrappers.append(CardWrapper(c, status_dict[c.id]))
		return wrappers

	@staticmethod
	def get_dict_by_name():
		wrappers = CardWrapper.get_cards()
		card_dict = {}
		for c in wrappers:
			card_dict[c.name.lower()] = c
		return card_dict

	@staticmethod
	def get_dict_by_id():
		wrappers = CardWrapper.get_cards()
		card_dict = {}
		for c in wrappers:
			card_dict[c.card.id] = c
		return card_dict

	@staticmethod
	def get_cards_by_id(ids):
		dict = CardWrapper.get_dict_by_id()
		matches = []
		for id in ids:
			matches.append(dict.get(id))
		return matches

	@staticmethod
	def filter_cards_by_status(wrappers):
		status_dict = defaultdict(list)
		for w in wrappers:
			status_dict[w.current_status.status].append(w)
		return status_dict

	@staticmethod
	def get_card(name):
		return CardWrapper.get_dict_by_name().get(name.lower())
		
class CardChecker():

	def __init__(self):
		self.cards = CardWrapper.get_dict_by_name()
		
	def get_id(self, name):
		wrapper = self.cards.get(name.lower())
		if wrapper:
			return wrapper.card.id
		return None