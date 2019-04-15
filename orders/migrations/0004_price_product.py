# Generated by Django 2.0.3 on 2019-04-14 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('orders', '0003_auto_20190413_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='priced_product', to='orders.Product'),
        ),
    ]
