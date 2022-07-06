from django.contrib import admin
from muzsport.models import *
from django.contrib.auth.models import Group


# class TrackAdmin(admin.ModelAdmin):
#     fields = ['file', 'photo', 'title', 'price']
#     list_filter = ['title']
#
# admin.site.register(Track, TrackAdmin)

admin.site.register(AdBigPhotoFile)
admin.site.register(AdSmallPhotoFile)
admin.site.register(Track)
admin.site.register(Coupons)
admin.site.register(Order)
admin.site.unregister(Group)
admin.site.register(Sports)
admin.site.register(Tags)
admin.site.register(Moods)
admin.site.register(Country)
admin.site.register(OrderSegmentDelete)
admin.site.register(OrderSegmentAdd)
admin.site.register(Wishlist)
admin.site.register(User)
admin.site.register(DirectionMusic)
admin.site.register(Footer)
admin.site.register(PaymentIcons)
admin.site.register(PriceModificationAndServices)







