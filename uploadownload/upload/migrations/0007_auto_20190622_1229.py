# Generated by Django 2.2.2 on 2019-06-22 12:29

from django.db import migrations, models
import upload.models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0006_auto_20190527_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='image',
            field=models.FileField(blank=True, default=None, null=True, upload_to=upload.models.upload_unique_loc),
        ),
    ]