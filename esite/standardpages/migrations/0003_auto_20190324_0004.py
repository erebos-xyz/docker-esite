# Generated by Django 2.1.7 on 2019-03-24 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('standardpages', '0002_auto_20190323_2357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='standardpage',
            old_name='image_caption',
            new_name='featured_image_caption',
        ),
    ]