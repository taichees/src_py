# Generated by Django 5.1.1 on 2024-11-01 13:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20241009_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('userName', models.TextField()),
                ('password', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contents',
            fields=[
                ('contentId', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.users')),
            ],
        ),
    ]
