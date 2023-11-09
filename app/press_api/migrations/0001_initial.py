# Generated by Django 4.2.7 on 2023-11-09 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("category_name", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Journalist",
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
                ("name", models.CharField(max_length=255)),
                ("subscribers_count", models.IntegerField(default=0)),
                ("articles_count", models.IntegerField(default=0)),
                ("cheer_count", models.IntegerField(default=0)),
                ("journalist_id", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="SubscribersGender",
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
                        on_delete=django.db.models.deletion.CASCADE,
                        to="press_api.journalist",
                        to_field="journalist_id",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SubscribersAge",
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
                (
                    "Journalists",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="press_api.journalist",
                        to_field="journalist_id",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sections",
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
                ("section_name", models.CharField(max_length=255, unique=True)),
                (
                    "journalist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="press_api.journalist",
                        to_field="journalist_id",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Press",
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
                ("press_name", models.CharField(max_length=255, unique=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="press_api.category",
                        to_field="category_name",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="journalist",
            name="press",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="press_api.press",
                to_field="press_name",
            ),
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
                        on_delete=django.db.models.deletion.CASCADE,
                        to="press_api.journalist",
                        to_field="journalist_id",
                    ),
                ),
                (
                    "section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="press_api.sections",
                        to_field="section_name",
                    ),
                ),
            ],
            options={
                "unique_together": {("journalist", "section")},
            },
        ),
    ]
