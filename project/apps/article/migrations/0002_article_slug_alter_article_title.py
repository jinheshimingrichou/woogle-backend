# Generated by Django 4.2.3 on 2024-04-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=250, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='', max_length=250),
        ),
    ]
