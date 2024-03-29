# Generated by Django 3.2.23 on 2024-02-02 09:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0005_userrecord_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrecord',
            name='username',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='associated_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
