# Generated by Django 5.1.5 on 2025-01-31 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_profilemodel_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
