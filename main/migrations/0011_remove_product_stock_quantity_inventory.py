# Generated by Django 4.2.13 on 2024-06-16 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_shoppingcartitem_shoppingcart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock_quantity',
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_quantity', models.PositiveIntegerField()),
                ('last_update_time', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
    ]
