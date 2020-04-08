from statshandling.serializers import GenericStatSerializer

from .models import NewsStat, CommentsStat, RSSParserStat, UsersStat


class NewsStatSerializer(GenericStatSerializer):

    class Meta:
        model = NewsStat


class CommentsStatSerializer(GenericStatSerializer):

    class Meta:
        model = CommentsStat

class RSSParserStatSerializer(GenericStatSerializer):

    class Meta:
        model = RSSParserStat

class UsersStatsSerializer(GenericStatSerializer):

    class Meta:
        model = UsersStatsSerializer