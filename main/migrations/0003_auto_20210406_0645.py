# Generated by Django 3.1 on 2021-04-06 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210406_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='week',
            name='schedule',
            field=models.TextField(blank=True),
        ),
    ]
