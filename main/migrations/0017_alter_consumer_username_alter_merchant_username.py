# Generated by Django 4.2.13 on 2024-06-19 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_consumer_last_login_alter_merchant_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]