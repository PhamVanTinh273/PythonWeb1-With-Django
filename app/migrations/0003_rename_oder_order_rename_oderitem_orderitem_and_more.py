# Generated by Django 5.0 on 2024-03-14 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Oder',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='OderItem',
            new_name='OrderItem',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='date_oder',
            new_name='date_order',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='oder',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='oder',
            new_name='order',
        ),
    ]
