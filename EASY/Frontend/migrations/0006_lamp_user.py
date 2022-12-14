# Generated by Django 4.1.3 on 2022-12-22 10:35

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Frontend', '0005_alter_lamp_lamp_name'),
    ]

    operations = [
        migrations.DeleteModel(name='Lamp'),
        migrations.CreateModel(
            name='Lamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lamp_name', models.CharField(default='Lamp name', max_length=200)),
                ('time_set_on', models.TimeField(default='00:00:00')),
                ('time_set_off', models.TimeField(default='00:00:00')),
                ('user',
                 models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE,
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Lamps',
            },
        ),
    ]
