# Generated by Django 4.0.3 on 2022-04-18 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_todo_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='items',
        ),
        migrations.CreateModel(
            name='ToDoListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('todo_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='todo.todo')),
            ],
        ),
    ]
