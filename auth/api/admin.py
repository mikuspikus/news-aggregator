from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    AuthUser,
    UserAuthToken,
    ServicesToken
)


admin.site.register(AuthUser, UserAdmin)


class UserAuthTokenAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserAuthToken, UserAuthTokenAdmin)


class ServicesTokenAdmin(admin.ModelAdmin):
    pass


admin.site.register(ServicesToken, ServicesTokenAdmin)