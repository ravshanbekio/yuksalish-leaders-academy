# Generated by Django 3.2.9 on 2021-12-27 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('YuksalishApp', '0013_alter_contact_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=150, verbose_name='Shahar/tuman')),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='YuksalishApp.city'),
        ),
    ]
