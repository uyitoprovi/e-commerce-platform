# Generated by Django 5.1 on 2024-09-17 07:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={"ordering": ["-created"]},
        ),
        migrations.AddIndex(
            model_name="order",
            index=models.Index(
                fields=["-created"], name="orders_orde_created_743fca_idx"
            ),
        ),
    ]
