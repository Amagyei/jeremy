# Generated by Django 5.0.6 on 2024-05-31 12:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chicken", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chicken",
            name="name",
            field=models.CharField(default="chicken", max_length=100, null=True),
        ),
    ]
