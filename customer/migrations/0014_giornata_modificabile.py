# Generated by Django 5.0.1 on 2024-09-21 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_giornata_intervento_giornata'),
    ]

    operations = [
        migrations.AddField(
            model_name='giornata',
            name='modificabile',
            field=models.BooleanField(default=True),
        ),
    ]