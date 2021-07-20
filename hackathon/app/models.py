from django.db import models

class Recruit(models.Model):
    name = models.CharField(max_length=200)