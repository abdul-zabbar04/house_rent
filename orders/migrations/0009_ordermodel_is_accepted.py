# Generated by Django 5.1.1 on 2024-10-05 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_ordermodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
    ]
