# Generated by Django 4.1.5 on 2023-02-06 10:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_todo_created_at_alter_todo_uid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('518f7c09-24dc-4d1d-a577-0ac07ed6db53'), editable=False, primary_key=True, serialize=False),
        ),
    ]
