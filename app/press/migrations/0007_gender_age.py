# Generated by Django 4.2.7 on 2023-11-10 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("press", "0006_alter_journalist_press"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gender",
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
                ("gender", models.CharField(max_length=1)),
                ("percentage", models.IntegerField(default=0)),
                (
                    "journalist",
                    models.ForeignKey(
                        db_column="journalist_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="press.journalist",
                        to_field="journalist_id",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Age",
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
                ("age", models.IntegerField(default=0)),
                ("percentage", models.IntegerField(default=0)),
                (
                    "journalist",
                    models.ForeignKey(
                        db_column="journalist_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="press.journalist",
                        to_field="journalist_id",
                    ),
                ),
            ],
        ),
    ]
