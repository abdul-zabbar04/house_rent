# Generated by Django 5.1.1 on 2024-09-23 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_reviewmodel_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='is_order',
            field=models.BooleanField(default=False),
        ),
    ]
