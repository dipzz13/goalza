# Generated by Django 2.2 on 2019-05-08 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20190507_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='duration',
            field=models.DurationField(),
        ),
    ]