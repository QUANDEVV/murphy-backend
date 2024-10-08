# Generated by Django 5.0.6 on 2024-06-18 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0009_alter_photo_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subname', models.CharField(default='Default Subname', max_length=100)),
                ('bio', models.TextField()),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='Ai-Girls')),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='Ai-Girls')),
                ('subscription_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('tips', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('online_status', models.BooleanField(default=False)),
                ('last_active', models.DateTimeField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('likes_count', models.PositiveIntegerField(default=0)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
            ],
        ),
    ]
