from django.db import models


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=255, unique=True, null=False)


class Press(models.Model):
    press_id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, to_field='category_id', null=False)
    name = models.CharField(max_length=255, unique=True, null=False)


class Journalist(models.Model):
    press = models.ForeignKey(Press, on_delete=models.CASCADE, to_field='press_id', null=False)
    journalist_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    subscribers_count = models.IntegerField(default=0)
    articles_count = models.IntegerField(default=0)
    cheer_count = models.IntegerField(default=0)


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
