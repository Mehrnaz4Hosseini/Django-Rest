# Generated by Django 4.1.3 on 2024-03-02 16:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_product_featured_alter_product_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="featured",
            field=models.BooleanField(default=True),
        ),
    ]
