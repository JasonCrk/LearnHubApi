# Generated by Django 5.0.6 on 2024-06-17 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assigned_homework', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignedhomework',
            name='grade',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
