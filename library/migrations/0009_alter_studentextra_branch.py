# Generated by Django 5.0.7 on 2024-07-14 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20200412_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentextra',
            name='branch',
            field=models.CharField(choices=[('it', 'IT'), ('cse', 'CSE'), ('ec', 'EC'), ('ce', 'CE'), ('bba', 'BBA')], max_length=40),
        ),
    ]