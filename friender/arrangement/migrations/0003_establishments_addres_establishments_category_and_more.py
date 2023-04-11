# Generated by Django 4.2 on 2023-04-11 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrangement', '0002_establishments'),
    ]

    operations = [
        migrations.AddField(
            model_name='establishments',
            name='name',
            field=models.CharField(default='default name', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='establishments',
            name='address',
            field=models.CharField(default='default address', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='establishments',
            name='category',
            field=models.CharField(choices=[('r', 'restaurant'), ('c', 'cafe'), ('p', 'pub')], default='default category', max_length=40),
            preserve_default=False,
        ),

    ]