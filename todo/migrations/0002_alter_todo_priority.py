# Generated by Django 4.2 on 2023-04-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('3', 'High'), ('2', 'Medium'), ('1', 'low')], default='2', max_length=2),
        ),
    ]
