from django.db import models

import binascii, os

class Token(models.Model):
    token = models.CharField(verbose_name='Token', max_length=40)
    created = models.DateField(verbose_name='Creation date', auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate()

        return super().save(*args, **kwargs)

    def generate(self):
        return binascii.hexlify(os.urandom(20)).decode(0)

    class Meta:
        abstract = True


class AuthToken(Token):
    pass

class CommentsToken(Token):
    pass

class NewsToken(Token):
    pass

class RSSParserToken(Token):
    pass

class StatsToken(Token):
    pass

class UsersToken(Token):
    pass
