# Generated by Django 5.2.3 on 2025-06-23 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("house", "0006_type_addvillaapartment"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomerReview",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
                ("profession", models.CharField(max_length=200)),
                ("image", models.ImageField(upload_to="house/images/rivews")),
                ("description", models.TextField()),
            ],
        ),
    ]
