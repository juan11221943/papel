# Generated by Django 2.2.3 on 2019-07-23 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0006_auto_20190711_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.Producto'),
        ),
    ]