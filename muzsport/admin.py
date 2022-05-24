from django.contrib import admin
from muzsport.models import *
from django.contrib.auth.models import Group

admin.site.register(Track)
admin.site.register(Coupons)
admin.site.register(Order)
admin.site.unregister(Group)
admin.site.register(Sports)
admin.site.register(Tags)
admin.site.register(Moods)
admin.site.register(Country)

