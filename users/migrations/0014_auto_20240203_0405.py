# Generated by Django 3.2.23 on 2024-02-02 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_merge_0012_auto_20240202_2342_0012_problem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='problem',
            name='time',
            field=models.TimeField(),
        ),
    ]
