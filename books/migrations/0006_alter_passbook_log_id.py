# Generated by Django 3.2.9 on 2021-11-23 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_passbook_log_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passbook',
            name='log_id',
            field=models.PositiveIntegerField(auto_created=True, unique=True),
        ),
    ]
