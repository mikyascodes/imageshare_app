# Generated by Django 4.2.3 on 2024-02-19 18:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagepage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='default.jpg', upload_to='uploads/')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=255)),
                ('post_date', models.DateTimeField(default=datetime.datetime.now)),
                ('user_name', models.CharField(max_length=20)),
            ],
        ),
    ]
