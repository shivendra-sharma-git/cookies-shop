# Generated by Django 3.1.1 on 2020-09-25 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookies', '0004_cookie_imagepath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cookie',
            name='imagepath',
            field=models.CharField(max_length=200),
        ),
    ]
