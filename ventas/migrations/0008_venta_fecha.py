# Generated by Django 2.2.3 on 2019-07-23 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0007_auto_20190723_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]