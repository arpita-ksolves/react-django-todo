# Generated by Django 4.0.3 on 2022-04-19 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_todo_items_todolistitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='ToDoList',
        ),
    ]
