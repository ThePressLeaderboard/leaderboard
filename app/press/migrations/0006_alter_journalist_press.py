# Generated by Django 4.2.7 on 2023-11-10 08:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("press", "0005_alter_press_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="journalist",
            name="press",
            field=models.ForeignKey(
                db_column="press_name",
                on_delete=django.db.models.deletion.CASCADE,
                to="press.press",
                to_field="press_name",
            ),
        ),
    ]
