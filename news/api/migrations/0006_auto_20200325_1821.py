# Generated by Django 3.0.3 on 2020-03-25 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200325_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='direction',
        ),
        migrations.AddField(
            model_name='vote',
            name='is_up',
            field=models.BooleanField(choices=[(True, 'up'), (False, 'down')], default=True),
        ),
    ]
