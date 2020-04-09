from statshandling.serializers import GenericStatSerializer

from .models import NewsStat, CommentsStat, RSSParserStat, UsersStat


class NewsStatSerializer(GenericStatSerializer):

    class Meta:
        model = NewsStat
        fields = '__all__'


class CommentsStatSerializer(GenericStatSerializer):

    class Meta:
        model = CommentsStat
        fields = '__all__'

class RSSParserStatSerializer(GenericStatSerializer):

    class Meta:
        model = RSSParserStat
        fields = '__all__'

class UsersStatsSerializer(GenericStatSerializer):

    class Meta:
        model = UsersStat
        fields = '__all__'