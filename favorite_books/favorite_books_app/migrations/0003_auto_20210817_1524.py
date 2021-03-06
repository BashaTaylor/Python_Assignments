# Generated by Django 2.2 on 2021-08-17 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_books_app', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='users_who_like',
            field=models.ManyToManyField(related_name='liked_books', to='favorite_books_app.User'),
        ),
    ]
