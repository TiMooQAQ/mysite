# Generated by Django 3.1 on 2020-08-17 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200817_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='封面/%Y%m%d', verbose_name='封面'),
        ),
    ]
