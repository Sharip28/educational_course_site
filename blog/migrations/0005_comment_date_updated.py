# Generated by Django 3.1 on 2021-04-07 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
