# Generated by Django 5.0.6 on 2024-07-27 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_employee_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.CharField(default='lbrsibs', max_length=100),
        ),
    ]
