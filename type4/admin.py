from django.contrib import admin
from type4.models import Card, Status
from datetime import date
                                    
class StatusInline(admin.StackedInline):
	model = Status
	extra = 1
	
class CardAdmin(admin.ModelAdmin):
	inlines = [StatusInline]
	flags = Card.flags()
	fieldsets = [
		(None,		{'fields': ['name']}),
		('Flags',	{'fields': flags}),
	]
 	list_display = ['name', 'current_status'] + flags
 	list_filter = flags
	search_fields = ['name']


admin.site.register(Card, CardAdmin)
