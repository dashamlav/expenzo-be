# Generated by Django 3.2.9 on 2022-01-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, unique=True),
        ),
    ]