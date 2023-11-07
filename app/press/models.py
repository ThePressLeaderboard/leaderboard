from django.db import models


class Press(models.Model):
    press_id = models.CharField(max_length=4)
    name = models.CharField(max_length=4)