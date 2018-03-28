from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.auth.forms import UserChangeForm


class MyUserAdmin(UserAdmin):
    model = User


    list_display = ('username','is_blogger', 'email')
    list_filter = ('is_blogger',)
    fieldsets = UserAdmin.fieldsets + (
        (('Extra info', {'fields': ('bio', 'is_blogger')}),
    ))


admin.site.register(User, MyUserAdmin)


