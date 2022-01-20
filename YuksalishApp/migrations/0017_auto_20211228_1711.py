# Generated by Django 3.2.9 on 2021-12-28 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('YuksalishApp', '0016_auto_20211228_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=150, verbose_name='Shahar/tuman')),
                ('address', models.CharField(max_length=200, verbose_name='Manzil')),
                ('phone', models.CharField(max_length=13, verbose_name='Telefon raqam')),
            ],
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ManyToManyField(to='YuksalishApp.City')),
                ('viloyat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YuksalishApp.location')),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='YuksalishApp.city'),
        ),
    ]
