# Generated by Django 2.2.3 on 2019-07-24 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0009_auto_20190723_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='total_parcial',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
