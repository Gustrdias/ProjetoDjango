# Generated by Django 3.2.5 on 2021-07-04 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seriado', '0002_seriado_imagemfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seriado',
            name='imagemFile',
            field=models.FileField(upload_to='path'),
        ),
    ]
