# Generated by Django 4.2.16 on 2024-10-29 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashbordapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
