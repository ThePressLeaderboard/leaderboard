# Generated by Django 4.2.7 on 2023-11-07 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Press',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('press_id', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=4)),
            ],
        ),
    ]
