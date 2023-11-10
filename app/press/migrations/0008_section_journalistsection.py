# Generated by Django 4.2.7 on 2023-11-10 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("press", "0007_gender_age"),
    ]

    operations = [
        migrations.CreateModel(
            name="Section",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("section_name", models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="JournalistSection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "journalist",
                    models.ForeignKey(
                        db_column="journalist_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="press.journalist",
                        to_field="journalist_id",
                    ),
                ),
                (
                    "section",
                    models.ForeignKey(
                        db_column="section_name",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="press.section",
                        to_field="section_name",
                    ),
                ),
            ],
            options={
                "unique_together": {("journalist", "section")},
            },
        ),
    ]
