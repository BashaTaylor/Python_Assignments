# Generated by Django 2.2 on 2021-08-19 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_books_app', '0003_auto_20210817_1524'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookManager',
        ),
    ]