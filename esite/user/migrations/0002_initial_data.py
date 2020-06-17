# -*- coding: utf-8 -*-
from django.db import migrations
from django.contrib.auth import get_user_model


def create_anonuser(apps, schema_editor):
    # Get models
    User = get_user_model()

    # Create anonymous user
    anonuser = User.objects.create(
        username="cisco",
        is_customer=False,
    )

    anonuser.set_password("ciscocisco")

    anonuser.save()

def remove_anonuser(apps, schema_editor):
    # Get models
    User = get_user_model()

    # Delete the anonymous user
    User.objects.get(username="cisco").delete()

def create_adminuser(apps, schema_editor):
    # Get models
    User = get_user_model()

    # Create anonymous user
    anonuser = User.objects.create(
        username="admin",
        is_customer=False,
    )

    adminuser.set_password("ciscocisco")

    adminuser.save()

def remove_adminuser(apps, schema_editor):
    # Get models
    User = get_user_model()

    # Delete the anonymous user
    User.objects.get(username="admin").delete()


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_anonuser, remove_anonuser, create_adminuser, remove_adminuser),
    ]