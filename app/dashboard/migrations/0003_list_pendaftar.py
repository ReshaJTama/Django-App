# Generated by Django 3.2.4 on 2021-06-12 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20210612_0109'),
    ]

    operations = [
        migrations.CreateModel(
            name='List_pendaftar',
            fields=[
                ('nis', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('desc', models.CharField(max_length=500)),
                ('ibu', models.CharField(max_length=500)),
                ('ayah', models.CharField(max_length=500)),
                ('domisili', models.CharField(max_length=500)),
                ('telp', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('asal', models.CharField(max_length=500)),
            ],
        ),
    ]
