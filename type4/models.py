from django.db import models

import logging
logger = logging.getLogger(__name__)


class Card(models.Model):

    # fields
    name = models.CharField(max_length=100)
    is_instant = models.BooleanField('is instant or has flash', default=False)
    is_wrath = models.BooleanField('is one-shot mass removal or bounce', default=False)
    is_burn = models.BooleanField('burns players', default=False)
    is_lifegain = models.BooleanField('gives life', default=False)
    is_creature_fat = models.BooleanField('permanent: creature with combined p/t >= 14', default=False)
    is_creature_threat = models.BooleanField('permanent: creature with power >= 4', default=False)
    is_creature = models.BooleanField('permanent: creature', default=False)
    is_artifact = models.BooleanField('permanent: artifact', default=False)
    is_enchantment = models.BooleanField('permanent: enchantment', default=False)
    is_land = models.BooleanField('permanent: land', default=False)
    is_counterspell = models.BooleanField('counters spells', default=False)
    is_masticore = models.BooleanField('masticore', default=False)
    is_draw = models.BooleanField('generates 2+ card advantage', default=False)
    is_removal_creature = models.BooleanField('kills: creatures', default=False)
    is_removal_artifact = models.BooleanField('kills: artifacts', default=False)
    is_removal_enchantment = models.BooleanField('kills: enchantments', default=False)
    is_removal_land = models.BooleanField('kills: land', default=False)    
    is_confiscate = models.BooleanField('takes cards belonging to other people', default=False)    
    is_morph = models.BooleanField('morphs', default=False)
    is_recurring = models.BooleanField('has buyback or some other recurring effect', default=False)
    is_cycling = models.BooleanField('has cycling', default=False)
    is_reanimate = models.BooleanField('reanimates', default=False)
    is_flash_enabler = models.BooleanField('gives other cards flash', default=False)
    is_hard_to_kill = models.BooleanField('is hard to kill', default=False)
    is_stack_specific = models.BooleanField('works best when played Stack format', default=False)

    # for use only by admin site
    def current_status(self):
        recent_statuses = Status.objects.filter(card_id=self.id).order_by('-timestamp')
        if recent_statuses:
            return recent_statuses[0].status
        return None

    def __unicode__(self):
        return self.name

    @staticmethod
    def flags():
        return list(n for n in Card._meta.get_all_field_names() if n.startswith('is_'))


class Status(models.Model):

    # status enum
    IN_STACK = 1
    GOING_IN_STACK = 2
    REMOVED_FROM_STACK = 3
    REJECTED_FROM_STACK = 4
    STATUS_CHOICES = (
        (IN_STACK, 'Currently in stack'),
        (GOING_IN_STACK, 'Waiting to be added'),
        (REMOVED_FROM_STACK, 'Playtested and then removed'),
        (REJECTED_FROM_STACK, 'Do NOT intend to try'),
    )

    # fields
    card = models.ForeignKey(Card)
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=IN_STACK)
    timestamp = models.DateTimeField('timestamp')

    # funcs
    def status_choices(self):
        choices = []
        for c in self.STATUS_CHOICES:
            s = StatusChoice()
            s.id = c[0]
            s.name = c[1]
            choices.append(s)
        return choices

    def is_in_stack(self):
        return self.status == self.IN_STACK

    def __unicode__(self):
        str = ''
        if not self.is_in_stack():
            str = 'NOT '
        return (
            self.card.name
            + ' is '
            + str
            + 'in the stack'
        )


class StatusChoice():
    name = ''
    id = 0


class FilterChoice():
    name = ''
    attr = ''

    @staticmethod
    def get():
        flag_set = Card.flags()
        filter_choices = []
        for f in flag_set:
            filter = FilterChoice()
            filter.name = Card._meta.get_field(f).verbose_name
            filter.attr = f
            filter_choices.append(filter)
        filter_choices = sorted(filter_choices, key=lambda c: c.name)
        return filter_choices


class CategoryCount():
    name = ''
    attr = ''
    count = 0
    percent = 0
    active = False
