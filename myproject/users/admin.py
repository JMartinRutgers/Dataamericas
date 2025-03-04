from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Add any custom fields to these lists
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    fieldsets = UserAdmin.fieldsets
    # If you have custom fields, add them like this:
    # fieldsets = UserAdmin.fieldsets + (
    #     ('Custom Fields', {'fields': ('custom_field1', 'custom_field2')}),
    # )

# Register with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)