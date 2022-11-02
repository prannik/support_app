from django.contrib import admin

from app.account.models import CustomUser

admin.site.register(CustomUser)
