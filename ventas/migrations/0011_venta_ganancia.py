# Generated by Django 2.2.3 on 2019-07-24 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0010_venta_total_parcial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='ganancia',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
