# Generated by Django 5.1.4 on 2025-01-25 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_app', '0016_subtasks_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtasks',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='join_app.task'),
        ),
    ]
