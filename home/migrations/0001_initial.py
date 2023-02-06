# Generated by Django 4.1.5 on 2023-02-06 09:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('updated_at', models.DateField(auto_created=True)),
                ('created_at', models.DateField(auto_created=True)),
                ('uid', models.UUIDField(default=uuid.UUID('d31efb3d-e537-4a68-99d3-2fe797548238'), editable=False, primary_key=True, serialize=False)),
                ('todo_title', models.CharField(max_length=100)),
                ('todo_description', models.TextField()),
                ('is_done', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
