# Generated by Django 4.2.1 on 2023-06-03 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalityApp', '0007_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
