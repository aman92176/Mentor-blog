# Generated by Django 2.2.10 on 2020-03-31 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
