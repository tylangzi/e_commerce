# Generated by Django 4.2.13 on 2024-06-18 01:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_consumer_password_alter_consumer_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='merchant',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
