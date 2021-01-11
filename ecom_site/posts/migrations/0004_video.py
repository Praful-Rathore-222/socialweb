# Generated by Django 3.1.4 on 2021-01-05 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_auto_20210105_1143"),
    ]

    operations = [
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=500)),
                (
                    "videofile",
                    models.FileField(null=True, upload_to="videos/", verbose_name=""),
                ),
            ],
        ),
    ]
