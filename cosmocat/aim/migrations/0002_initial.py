# Generated by Django 5.1.3 on 2024-11-20 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aim', '0001_initial'),
        ('mission', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aim',
            name='mission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='targets', to='mission.mission'),
        ),
    ]