# Generated by Django 4.1.3 on 2024-03-07 09:01

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Review",
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
                ("user_id", models.IntegerField()),
                ("product_id", models.IntegerField()),
                ("title", models.CharField(max_length=100)),
                ("body", models.TextField()),
                ("rating", models.IntegerField()),
                ("date_posted", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]