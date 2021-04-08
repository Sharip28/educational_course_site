# Generated by Django 3.1 on 2021-04-07 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='experience',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='language',
            field=models.CharField(blank=True, choices=[('python', 'Python'), ('javascript', 'Javascript')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]