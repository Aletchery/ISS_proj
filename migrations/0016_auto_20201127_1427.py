# Generated by Django 3.1.3 on 2020-11-27 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivals', '0015_auto_20201126_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_festival',
            name='obrazok',
            field=models.CharField(max_length=255),
        ),
    ]
