# Generated by Django 3.2.9 on 2021-11-20 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_staff',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
