# Generated by Django 5.0.6 on 2024-07-04 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
