# Generated by Django 2.2.4 on 2020-02-28 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20200227_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='cost',
            field=models.FloatField(default=0),
        ),
    ]
