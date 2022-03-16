# Generated by Django 3.2.12 on 2022-03-12 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='number',
        ),
        migrations.AddField(
            model_name='newuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newuser',
            name='secret',
            field=models.CharField(default='nothing', max_length=200),
        ),
    ]