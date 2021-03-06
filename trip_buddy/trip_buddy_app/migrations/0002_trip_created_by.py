# Generated by Django 2.2 on 2021-08-26 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trip_buddy_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='trip_submitter', to='trip_buddy_app.User'),
            preserve_default=False,
        ),
    ]
