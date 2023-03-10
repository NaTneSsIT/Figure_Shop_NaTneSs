# Generated by Django 4.1.5 on 2023-01-16 06:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_product_image"),
    ]

    operations = [
        migrations.RemoveField(model_name="orderitem", name="created_at",),
        migrations.RemoveField(model_name="shippingaddress", name="created_at",),
        migrations.AddField(
            model_name="orderitem",
            name="create_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="shippingaddress",
            name="create_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="order",
            name="create_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="update_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
