# Generated by Django 4.2.13 on 2024-05-21 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='tags',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]