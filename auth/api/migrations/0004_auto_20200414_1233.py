# Generated by Django 3.0.3 on 2020-04-14 12:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200324_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
