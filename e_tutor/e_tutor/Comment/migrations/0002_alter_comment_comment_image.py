# Generated by Django 4.2.2 on 2023-06-26 12:54

import Comment.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_image',
            field=models.ImageField(blank=True, null=True, upload_to=Comment.models.nameFile),
        ),
    ]
