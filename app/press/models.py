from django.db import models


class Category(models.Model):
    categoryName = models.CharField(max_length=255)


class Press(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Journalists(models.Model):
    press = models.ForeignKey(Press, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    subscribers_count = models.IntegerField(default=0)
    articles_count = models.IntegerField(default=0)
    cheer_count = models.IntegerField(default=0)
    sections = models.manyToManyField("Sections")


class SubscribersGender(models.Model):
    journalist = models.ForeignKey(Journalists, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1)
    percentage = models.IntegerField(default=0)


class SubscribersAge(models.Model):
    Journalists = models.ForeignKey(Journalists, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)


class Sections(models.Model):
    section_name = models.CharField(max_length=255)
