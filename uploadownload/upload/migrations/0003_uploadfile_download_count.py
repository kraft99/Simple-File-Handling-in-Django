# Generated by Django 2.1.7 on 2019-05-27 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20190526_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='download_count',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
