# Generated by Django 5.1.3 on 2024-11-20 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spycat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='experience',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]