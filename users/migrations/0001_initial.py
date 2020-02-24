# Generated by Django 2.2.4 on 2020-02-24 13:33

from django.db import migrations, models
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('Title', models.TextField(max_length=255)),
                ('Rating', models.DecimalField(decimal_places=0, max_digits=10)),
                ('Reviews', models.TextField()),
                ('Image', pyuploadcare.dj.models.ImageField(null=True)),
            ],
        ),
    ]
