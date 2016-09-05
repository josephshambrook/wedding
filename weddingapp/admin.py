from django.contrib import admin

from .models import Invite, Guest, Gift


class GuestInline(admin.TabularInline):
    model = Guest
    extra = 0
    min_num = 2


class InviteAdmin(admin.ModelAdmin):
    # define which columns show
    list_display = ('group_name', 'code', 'group_count',)
    # define which filters to show
    list_filter = ('code',)
    # show guest data inline
    inlines = [GuestInline]


class GuestAdmin(admin.ModelAdmin):
    # define which columns show
    list_display = ('guest_name', 'attending', 'diet', 'transport',)
    # define which filters to show
    list_filter = ('guest_name', 'invite', 'attending',)


class GiftAdmin(admin.ModelAdmin):
    list_display = ('item', 'url')


admin.site.register(Invite, InviteAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Gift, GiftAdmin)
