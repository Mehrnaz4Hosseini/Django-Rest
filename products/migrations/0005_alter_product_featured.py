# Generated by Django 4.1.3 on 2024-03-02 16:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_alter_product_featured"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="featured",
            field=models.BooleanField(null=True),
        ),
    ]
