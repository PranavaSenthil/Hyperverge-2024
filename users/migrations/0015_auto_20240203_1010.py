# Generated by Django 3.2.23 on 2024-02-03 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20240203_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='problem_discription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
