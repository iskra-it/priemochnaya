# Generated by Django 4.2 on 2023-11-25 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_attrvalue_attr_id_remove_attrvalue_case_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attrvalue',
            name='is_any',
            field=models.BooleanField(default=False),
        ),
    ]