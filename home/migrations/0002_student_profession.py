# Generated by Django 5.1.5 on 2025-01-23 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profession',
            field=models.TextField(blank=True, null=True),
        ),
    ]
