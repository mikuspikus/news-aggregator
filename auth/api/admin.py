from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AuthUser, AuthToken, UsersToken, NewsToken, CommentsToken, RSSParserToken, StatsToken


admin.site.register(AuthUser, UserAdmin)

class AuthTokenAdmin(admin.ModelAdmin):
    pass
admin.site.register(AuthToken, AuthTokenAdmin)

class UsersTokenAdmin(admin.ModelAdmin):
    pass
admin.site.register(UsersToken, UsersTokenAdmin)

class NewsTokenAdmin(admin.ModelAdmin):
    pass
admin.site.register(NewsToken, NewsTokenAdmin)

class CommentsTokenAdmin(admin.ModelAdmin):
    pass
admin.site.register(CommentsToken, CommentsTokenAdmin)

class RSSParserTokenAdmin(admin.ModelAdmin):
    pass
admin.site.register(RSSParserToken, RSSParserTokenAdmin)

class StatsTokenAdmin(admin.ModelAdmin):
    pass
admin.site.register(StatsToken, StatsTokenAdmin)