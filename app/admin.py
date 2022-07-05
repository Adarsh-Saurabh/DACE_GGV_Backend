from django.contrib import admin
from .models import Login

class LoginAdmin(admin.ModelAdmin):
    # Used to show the fields in the admin page
    list_display = [ 'name', 'registration_no', 'profile']
    # filters out the attributes with which we can perform search_fields
    list_filter = ['name', 'registration_no']
    # Creates a search box in the admin page
    search_fields = ['name', 'registration_no']

# Register your models here.
admin.site.register(Login, LoginAdmin)


