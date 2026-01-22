from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'state', 'city', 'country', 'is_staff')
    search_fields = ('username', 'email', 'phone')
    list_filter = ('state', 'city', 'country', 'is_staff')
