# Generated by Django 2.2.4 on 2020-02-29 04:12

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_games_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='image',
            field=pyuploadcare.dj.models.ImageField(null=True),
            preserve_default=False,
        ),
    ]
