# Generated by Django 5.0.6 on 2024-06-10 21:58

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='access_code',
            field=models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='Access code'),
        ),
    ]
