# Generated by Django 5.0.3 on 2024-04-23 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tanfelo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tanfelo_tanulocsoport',
            name='lehetseges_tantargyai',
            field=models.ManyToManyField(blank=True, null=True, to='app_tanfelo.tanfelo_tantargy'),
        ),
    ]
