# Generated by Django 2.0.3 on 2019-04-15 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_auto_20190415_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='productline',
            name='require_addons',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
