# Generated by Django 4.2.7 on 2023-11-21 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eventapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CreateEvent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("date", models.DateField()),
                ("location", models.CharField(max_length=200)),
                ("description", models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name="MyModel",
        ),
    ]
