from django.contrib import admin
from muzsport.models import Track, Coupons, Order
from django.contrib.auth.models import Group

admin.site.register(Track)
admin.site.register(Coupons)
admin.site.register(Order)
admin.site.unregister(Group)

