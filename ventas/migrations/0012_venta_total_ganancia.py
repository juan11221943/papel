# Generated by Django 2.2.3 on 2019-07-24 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0011_venta_ganancia'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='total_ganancia',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
