# Generated by Django 4.2 on 2023-11-25 18:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created on'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='case',
            name='name',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='case',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated on'),
        ),
        migrations.AlterField(
            model_name='attr',
            name='question',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='attrvalue',
            name='value',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='case',
            name='recommendation',
            field=models.TextField(blank=True),
        ),
    ]
