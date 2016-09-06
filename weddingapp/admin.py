from django.contrib import admin

from .models import Invite, Guest, Gift, Hotel


class GuestInline(admin.TabularInline):
    model = Guest
    extra = 0
    min_num = 2


class InviteAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'code', 'group_count')
    inlines = [GuestInline]


class GuestAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'attending', 'diet', 'transport')
    list_filter = ('attending', 'transport')


class GiftAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'actual', 'category', 'url')
    list_filter = ('category', 'actual')


class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'postcode', 'phone_number')


admin.site.register(Invite, InviteAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Gift, GiftAdmin)
admin.site.register(Hotel, HotelAdmin)
