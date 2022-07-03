from django.contrib import admin
from .models import MyUser, #Profile
from django.contrib.auth.models import Group
# Register your models here.

admin.site.register(MyUser)
#admin.site.register(Profile)

admin.site.unregister(Group)




