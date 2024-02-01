# Generated by Django 5.0.1 on 2024-02-01 16:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subadmins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('company_description', models.TextField()),
                ('company_address', models.CharField(max_length=100)),
                ('company_city', models.CharField(max_length=100)),
                ('company_state', models.CharField(max_length=100)),
                ('company_district', models.CharField(max_length=100)),
                ('comapany_area', models.CharField(max_length=100)),
                ('company_pincode', models.CharField(max_length=6)),
                ('comapany_image', models.ImageField(upload_to='company_images')),
                ('working_hrs', models.IntegerField()),
                ('holidays', models.PositiveSmallIntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], default=None)),
                ('service_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.servicetype')),
            ],
        ),
        migrations.CreateModel(
            name='ratings_reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('review', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.subadmins')),
            ],
        ),
        migrations.CreateModel(
            name='UserRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phoneNo', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='images/')),
                ('address', models.TextField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('pincode', models.CharField(max_length=6)),
                ('is_active', models.BooleanField(default=False)),
                ('is_super_admin', models.BooleanField(default=False)),
                ('service_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.servicetype')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='associated_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='subadmins',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userrecord'),
        ),
    ]
