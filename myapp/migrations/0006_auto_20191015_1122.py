# Generated by Django 2.2.6 on 2019-10-15 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20191015_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='microbitsummary',
            name='numberOfMicrobits',
            field=models.CharField(max_length=6),
        ),
    ]
