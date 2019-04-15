# Generated by Django 2.0.3 on 2019-04-14 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20190414_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productline',
            name='addOns',
        ),
        migrations.RemoveField(
            model_name='productline',
            name='toppings',
        ),
        migrations.AddField(
            model_name='addon',
            name='productlines',
            field=models.ManyToManyField(blank=True, related_name='subs_addOn', to='orders.Productline'),
        ),
        migrations.AddField(
            model_name='topping',
            name='productlines',
            field=models.ManyToManyField(blank=True, related_name='pizza_toppings', to='orders.Productline'),
        ),
    ]
