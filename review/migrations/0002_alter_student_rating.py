# Generated by Django 4.1.2 on 2022-11-17 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
    ]