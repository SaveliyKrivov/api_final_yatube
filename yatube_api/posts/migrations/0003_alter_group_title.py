# Generated by Django 5.2 on 2025-04-21 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_group_alter_comment_id_alter_post_id_post_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.TextField(max_length=200),
        ),
    ]
