# Generated by Django 3.2.9 on 2021-12-27 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YuksalishApp', '0010_auto_20211227_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(null=True, upload_to='img', verbose_name='Rasm'),
        ),
    ]
