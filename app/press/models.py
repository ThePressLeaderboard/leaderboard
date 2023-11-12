from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=20, unique=True)


class Press(models.Model):
    press_name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        to_field="category_name",
        db_column="category_name",
    )


class Journalist(models.Model):
    journalist_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=20)
    subscriber_count = models.IntegerField(default=0)
    article_count = models.IntegerField(default=0)
    cheer_count = models.IntegerField(default=0)

    press = models.ForeignKey(
        Press, on_delete=models.CASCADE, to_field="press_name", db_column="press_name"
    )


class Gender(models.Model):
    gender = models.CharField(max_length=1)
    percentage = models.IntegerField(default=0)

    journalist = models.ForeignKey(
        Journalist,
        on_delete=models.CASCADE,
        to_field="journalist_id",
        db_column="journalist_id",
    )


class Age(models.Model):
    age = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0)

    journalist = models.ForeignKey(
        Journalist,
        on_delete=models.CASCADE,
        to_field="journalist_id",
        db_column="journalist_id",
    )


class Section(models.Model):
    section_name = models.CharField(max_length=10, unique=True)


class JournalistSection(models.Model):
    journalist = models.ForeignKey(
        Journalist,
        on_delete=models.CASCADE,
        to_field="journalist_id",
        db_column="journalist_id",
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        to_field="section_name",
        db_column="section_name",
    )

    class Meta:
        unique_together = (("journalist", "section"),)
