from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Dining, DiningBooking, User, Listing, Order, OrderItem, Post, Donation, Partner, Document
class DocumentAdmin(admin.ModelAdmin):
    exclude = ('file_type',)

from django.contrib.auth.models import Group
from rest_framework_simplejwt.token_blacklist.models import (
    BlacklistedToken,
    OutstandingToken
)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('role', 'is_staff', 'is_active')
    ordering = ('email',)
    search_fields = ('email', 'first_name', 'last_name')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Roles', {'fields': ('role',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'role', 'password1', 'password2')}
        ),
    )

# admin.site.register(OrderItem)
admin.site.register(User, CustomUserAdmin)
admin.site.register([Listing, Order, Post, Donation, Partner, Dining, DiningBooking])
admin.site.register(Document, DocumentAdmin)

admin.site.unregister(Group)
admin.site.unregister(BlacklistedToken)
admin.site.unregister(OutstandingToken)
