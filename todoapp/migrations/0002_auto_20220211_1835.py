# Generated by Django 3.2.12 on 2022-02-12 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(default=False, max_length=200),
        ),
    ]