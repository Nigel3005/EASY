# Generated by Django 4.1.3 on 2022-11-26 21:55

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(choices=[('Starter', 'Starter'), ('Regular', 'Regular'), ('Advanced', 'Advanced')], default='Starter', max_length=20, unique=True)),
                ('plan_price', models.IntegerField(default=0)),
                ('number_off_areas', models.IntegerField(default=0)),
                ('number_off_lamps', models.IntegerField(default=0)),
                ('number_off_functions', models.IntegerField(default=0)),
                ('plan_description', models.TextField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Plans',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(choices=[('Starter', 'Starter'), ('Regular', 'Regular'), ('Advanced', 'Advanced')], default='Starter', max_length=20)),
                ('user', models.OneToOneField(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
