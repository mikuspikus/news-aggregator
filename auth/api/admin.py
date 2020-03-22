from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    AuthUser,
    AuthToken,
    AuthServiceToken,
    UsersServiceToken,
    NewsServiceToken,
    CommentsServiceToken,
    RSSParserServiceToken,
    StatsServiceToken,
)


admin.site.register(AuthUser, UserAdmin)


class AuthTokenAdmin(admin.ModelAdmin):
    pass


admin.site.register(AuthToken, AuthTokenAdmin)


class AuthServiceTokenAdmin(admin.ModelAdmin):
    pass


admin.site.register(AuthServiceToken, AuthServiceTokenAdmin)


class UsersServiceTokenAdmin(admin.ModelAdmin):
    pass


admin.site.register(UsersServiceToken, UsersServiceTokenAdmin)


class NewsServiceTokenAdmin(admin.ModelAdmin):
    pass


admin.site.register(NewsServiceToken, NewsServiceTokenAdmin)


class CommentsServiceTokenAdmin(admin.ModelAdmin):
    pass


admin.site.register(CommentsServiceToken, CommentsServiceTokenAdmin)


class RSSParserServiceTokenAdmin(admin.ModelAdmin):
    pass


admin.site.register(RSSParserServiceToken, RSSParserServiceTokenAdmin)


class StatsServiceTokenAdmin(admin.ModelAdmin):
    pass


admin.site.register(StatsServiceToken, StatsServiceTokenAdmin)
