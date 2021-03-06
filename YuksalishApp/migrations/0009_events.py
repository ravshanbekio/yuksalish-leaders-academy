# Generated by Django 3.2.9 on 2021-12-27 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YuksalishApp', '0008_delete_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viloyat', models.CharField(max_length=150, verbose_name='Viloyat')),
                ('city', models.CharField(max_length=200, verbose_name='Shahar/tuman')),
                ('address', models.CharField(max_length=150, verbose_name='Manzil')),
                ('phone', models.CharField(max_length=13, verbose_name='Telefon raqam')),
                ('image', models.ImageField(upload_to='img', verbose_name='Rasm')),
            ],
        ),
    ]
