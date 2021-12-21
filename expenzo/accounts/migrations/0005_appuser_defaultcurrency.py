# Generated by Django 3.2.9 on 2021-12-05 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_appuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='defaultCurrency',
            field=models.CharField(choices=[('inr', 'INR'), ('usd', 'USD'), ('eur', 'Euro'), ('pnd', 'Pound')], default='inr', max_length=3),
        ),
    ]