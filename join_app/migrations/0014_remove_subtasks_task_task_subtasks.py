# Generated by Django 5.1.4 on 2025-01-25 18:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_app', '0013_rename_subtask_subtasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtasks',
            name='task',
        ),
        migrations.AddField(
            model_name='task',
            name='subtasks',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='join_app.subtasks'),
        ),
    ]
