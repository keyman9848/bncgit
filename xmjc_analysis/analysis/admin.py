from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','userpass','useremail')

admin.site.register(User,UserAdmin)