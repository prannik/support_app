from django.contrib import admin

from app.account.models import CustomUser


class AccountAdmin(admin.ModelAdmin):
    pass


admin.site.register(CustomUser, AccountAdmin)
