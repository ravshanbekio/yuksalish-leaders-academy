# Generated by Django 3.2.9 on 2021-12-28 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YuksalishApp', '0018_general_null'),
    ]

    operations = [
        migrations.AlterField(
            model_name='general',
            name='null',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
