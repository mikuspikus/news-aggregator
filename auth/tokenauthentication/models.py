from django.db import models

import binascii, os

class Token(models.Model):
    token = models.CharField(verbose_name='Token', max_length=40, primary_key=True)
    created = models.DateTimeField(verbose_name='Creation date', auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate()

        return super().save(*args, **kwargs)

    def generate(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self) -> str:
        return f'Token <{self.token}:{self.created}>'

    class Meta:
        abstract = True