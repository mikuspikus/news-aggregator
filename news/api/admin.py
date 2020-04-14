from django.contrib import admin
from .models import News, User, Vote

class UserAdmin(admin.ModelAdmin):
    pass


class NewsAdmin(admin.ModelAdmin):
    pass


class VoteAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Vote, VoteAdmin)