# Generated by Django 4.2.13 on 2024-06-18 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_consumer_last_login_merchant_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='last_login',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='last_login',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
