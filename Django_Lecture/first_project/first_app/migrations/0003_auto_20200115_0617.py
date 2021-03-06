# Generated by Django 2.2.5 on 2020-01-15 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='eMail',
            field=models.EmailField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='firstName',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastName',
            field=models.CharField(max_length=128),
        ),
    ]
