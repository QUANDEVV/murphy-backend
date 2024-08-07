# Generated by Django 5.0.6 on 2024-06-18 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0010_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='creator',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_profile', to='rest.user'),
        ),
    ]
