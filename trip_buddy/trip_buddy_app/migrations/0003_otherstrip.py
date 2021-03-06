# Generated by Django 2.2 on 2021-08-26 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trip_buddy_app', '0002_trip_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='OthersTrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.TextField()),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now_add=True)),
                ('plan', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('join', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='join_trip_submitter', to='trip_buddy_app.Trip')),
            ],
        ),
    ]
