# Generated by Django 4.1.1 on 2023-02-01 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0003_remove_order_order_book_orderbook_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderbook',
            name='email_address',
        ),
        migrations.AddField(
            model_name='order',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
