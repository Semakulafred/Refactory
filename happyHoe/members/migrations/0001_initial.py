# Generated by Django 5.0.6 on 2024-09-16 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50, verbose_name='')),
            ],
        ),
    ]
