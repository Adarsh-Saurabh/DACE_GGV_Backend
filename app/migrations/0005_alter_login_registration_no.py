# Generated by Django 4.0.1 on 2022-07-05 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_login_registration_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='registration_no',
            field=models.CharField(max_length=50),
        ),
    ]
