# Generated by Django 3.1.4 on 2021-01-05 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0005_auto_20210105_1334"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="video",
            field=models.FileField(blank=True, upload_to="videos/"),
        ),
    ]
