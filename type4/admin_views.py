from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.utils import timezone
from type4.models import Card, Status
from type4.classes import CardWrapper, CardChecker
from type4.forms import ChangesForm
from django.core.exceptions import PermissionDenied

import logging
logger = logging.getLogger(__name__)

def __check_auth(request):
	authed = request.user.is_authenticated()
	logger.debug(authed)
	if not authed:
		raise PermissionDenied

def add_cards(request):
	__check_auth(request)
	
	status_set = Status().status_choices()
	flag_set = Card.flags()
	context = {'status_set': status_set, 'flag_set': flag_set}
	return render(request, 'type4/admin_add_cards.html', context)
    
def update(request):
	__check_auth(request)
	
	flag_set = Card.flags()
	flag_status = []
	for f in flag_set:
		s = request.POST[f]
		if s == 'True':
			flag_status.append({'flag_id': f, 'status':True})
		if s == 'False':
			flag_status.append({'flag_id': f, 'status':False})
	selected_status = request.POST['status']
	card_names = request.POST['card_names'].splitlines()
	checker = CardChecker()
	for n in card_names:
		id = checker.get_id(n)
		if id:
			new_card = Card.objects.get(id=id)
		else:
			new_card = Card()
			new_card.name = n
		for f in flag_status:
			setattr(new_card, f['flag_id'], f['status'])
		new_card.save()
		new_status = Status()
		new_status.card = new_card
		new_status.status = selected_status
		new_status.timestamp = timezone.now()
		new_status.save()
	return HttpResponseRedirect(reverse('type4:admin_add_cards'))
