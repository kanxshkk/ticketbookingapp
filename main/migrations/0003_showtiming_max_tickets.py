# Generated by Django 5.0.4 on 2024-04-13 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_movie_showtiming_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='showtiming',
            name='max_tickets',
            field=models.PositiveIntegerField(default=100),
        ),
    ]
