# Generated by Django 4.2.1 on 2023-06-03 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalityApp', '0006_prescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
