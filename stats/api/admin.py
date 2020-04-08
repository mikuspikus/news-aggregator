from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from  django.conf import settings

from .models import UsersStat, CommentsStat, RSSParserStat, NewsStat
from .download import report


FILENAME = getattr(settings, 'FILENAME', '{title}-{date}.xlsx')

__default_headers = ('User', 'Datetime', 'Action', 'Input data', 'Output data')
HEADERS = getattr(settings, 'HEADERS', __default_headers)

TITLE = getattr(settings, 'TITLE', 'Stats')


class UsersStatsAdmin(admin.ModelAdmin):
    actions = ('download_report', )

    def download_report(self, request: HttpRequest, queryset) -> HttpResponse:
        return report(queryset, '[user]-stats', HEADERS, FILENAME)
    download_report.short_description = "Download file for selected stats"

admin.site.register(UsersStat, UsersStatsAdmin)


class CommentsStatsAdmin(admin.ModelAdmin):
    actions = ('download_report', )

    def download_report(self, request: HttpRequest, queryset) -> HttpResponse:
        return report(queryset, '[comments]-stats', HEADERS, FILENAME)
    download_report.short_description = "Download file for selected stats"

admin.site.register(CommentsStat, CommentsStatsAdmin)

class RSSParserStatsAdmin(admin.ModelAdmin):
    actions = ('download_report', )

    def download_report(self, request: HttpRequest, queryset) -> HttpResponse:
        return report(queryset, '[rss-parser]-stats', HEADERS, FILENAME)
    download_report.short_description = "Download file for selected stats"

admin.site.register(RSSParserStat, RSSParserStatsAdmin)

class NewsStatsAdmin(admin.ModelAdmin):
    actions = ('download_report', )

    def download_report(self, request: HttpRequest, queryset) -> HttpResponse:
        return report(queryset, '[news]-stats', HEADERS, FILENAME)
    download_report.short_description = "Download file for selected stats"

admin.site.register(NewsStat, NewsStatsAdmin)