# Generated by Django 3.2.6 on 2021-08-25 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FarmItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=2083)),
                ('image_url', models.CharField(max_length=2083)),
                ('pdf_url', models.CharField(max_length=2083)),
            ],
        ),
    ]
