# Generated by Django 2.2.3 on 2019-07-10 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
                ('precio_compra', models.IntegerField()),
                ('precio_venta', models.IntegerField()),
            ],
        ),
    ]
