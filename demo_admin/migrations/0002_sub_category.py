# Generated by Django 5.0.2 on 2024-05-11 06:26

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_name', models.CharField(blank=True, max_length=10, null=True)),
                ('sub_category_image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('sub_category_code', models.CharField(blank=True, max_length=10, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='demo_admin.category')),
            ],
        ),
    ]
