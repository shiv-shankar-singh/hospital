# Generated by Django 4.2.7 on 2023-12-27 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='yourage',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mphone',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mpinno',
            field=models.CharField(max_length=25),
        ),
    ]