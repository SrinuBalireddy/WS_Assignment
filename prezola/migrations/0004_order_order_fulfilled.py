# Generated by Django 3.0.8 on 2020-08-01 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prezola', '0003_auto_20200801_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_fulfilled',
            field=models.BooleanField(default=False),
        ),
    ]