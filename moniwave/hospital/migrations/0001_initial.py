# Generated by Django 2.0.3 on 2018-05-09 09:33

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('name', models.CharField(max_length=254)),
                ('alias', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('name', models.CharField(max_length=254)),
                ('alias', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('name', models.CharField(max_length=254)),
                ('alias', models.CharField(max_length=10)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Hospital')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('name', models.CharField(max_length=254)),
                ('alias', models.CharField(max_length=10)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Service')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='bed',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Unit'),
        ),
    ]
