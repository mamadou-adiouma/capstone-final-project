from django.contrib import admin

from capstonefinalapp.models import MenuItem, Booking

# Register your models here.
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'image']

class BookingAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'reservation_date', 'phone_number', 'email']

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Booking, BookingAdmin)
