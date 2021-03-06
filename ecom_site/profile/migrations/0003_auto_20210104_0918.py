# Generated by Django 3.1.4 on 2021-01-04 09:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("profile", "0002_friendrequest"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="friends",
            field=models.ManyToManyField(
                blank=True, related_name="friends", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
