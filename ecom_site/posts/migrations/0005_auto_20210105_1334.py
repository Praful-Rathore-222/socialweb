# Generated by Django 3.1.4 on 2021-01-05 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_video"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="pic",
            field=models.ImageField(blank=True, upload_to="path/to/img"),
        ),
    ]
