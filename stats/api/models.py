from django.db import models

from statshandling.models import GenericStat


class UsersStat(GenericStat):
    pass


class NewsStat(GenericStat):
    pass


class CommentsStat(GenericStat):
    pass


class RSSParserStat(GenericStat):
    pass
