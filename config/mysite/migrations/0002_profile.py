# Generated by Django 4.2.2 on 2023-07-02 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('username', models.CharField(default='匿名ユーザー', max_length=100)),
                ('zipcode', models.CharField(default='', max_length=30)),
                ('prefecture', models.CharField(default='', max_length=6)),
                ('city', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
