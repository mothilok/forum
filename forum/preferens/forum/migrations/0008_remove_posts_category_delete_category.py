# Generated by Django 5.0.4 on 2024-10-07 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_rename_value_array_like_id_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
