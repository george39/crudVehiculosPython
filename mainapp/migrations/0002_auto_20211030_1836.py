# Generated by Django 3.0.5 on 2021-10-30 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
