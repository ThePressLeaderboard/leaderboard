from django.db import models
import csv


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True, null=False)


class Press(models.Model):
    press_name = models.CharField(max_length=255, unique=True, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, to_field='category_name', null=False)


class Journalist(models.Model):
    press = models.ForeignKey(Press, on_delete=models.CASCADE, to_field='press_name', null=False)
    name = models.CharField(max_length=255)
    subscribers_count = models.IntegerField(default=0)
    articles_count = models.IntegerField(default=0)
    cheer_count = models.IntegerField(default=0)
    journalist_id = models.CharField(max_length=255, unique=True, null=False)


class SubscribersGender(models.Model):
    journalist = models.ForeignKey(Journalist, on_delete=models.CASCADE, to_field='journalist_id', null=False)
    gender = models.CharField(max_length=1)
    percentage = models.IntegerField(default=0)


class SubscribersAge(models.Model):
    Journalists = models.ForeignKey(Journalist, on_delete=models.CASCADE, to_field='journalist_id', null=False)
    age = models.IntegerField(default=0)
    


class Sections(models.Model):
    section_name = models.CharField(max_length=255, unique=True, null=False)
    journalist = models.ForeignKey(Journalist, on_delete=models.CASCADE, to_field='journalist_id', null=False)


class JournalistSection(models.Model):
    journalist = models.ForeignKey(Journalist, on_delete=models.CASCADE, to_field='journalist_id', null=False)
    section = models.ForeignKey(Sections, on_delete=models.CASCADE, to_field='section_name', null=False)
    class Meta:
        unique_together = (('journalist', 'section'),)


def save_data_to_models():
    with open('../crawling/category.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # 첫 번째 줄은 헤더이므로 건너뜁니다.
        
        for row in reader:
            Category.objects.create(category_name=row[0].split(''))

    with open('../crawling/category.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # 첫 번째 줄은 헤더이므로 건너뜁니다.
        
        for row in reader:
            category = Category.objects.create(category_name=row[0])
        
save_data_to_models()
