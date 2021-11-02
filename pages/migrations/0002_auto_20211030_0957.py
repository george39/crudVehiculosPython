# Generated by Django 3.0.5 on 2021-10-30 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='color',
            field=models.CharField(default='null', max_length=50, verbose_name='color'),
        ),
        migrations.AddField(
            model_name='page',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='page',
            name='detail',
            field=models.CharField(default='null', max_length=50, verbose_name='detalles'),
        ),
        migrations.AddField(
            model_name='page',
            name='visible',
            field=models.BooleanField(default='null'),
        ),
        migrations.AlterField(
            model_name='page',
            name='brand',
            field=models.CharField(max_length=50, verbose_name='marca'),
        ),
        migrations.AlterField(
            model_name='page',
            name='line',
            field=models.CharField(max_length=50, verbose_name='linea'),
        ),
        migrations.AlterField(
            model_name='page',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=50, verbose_name='precio'),
        ),
    ]
