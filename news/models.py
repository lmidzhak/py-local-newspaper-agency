from django.contrib.auth.models import AbstractUser
from django.db import models


class Topic(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.username}"


class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    topics = models.ManyToManyField(Topic, related_name="articles")
    publishers = models.ManyToManyField(Redactor, related_name="articles")

    def __str__(self):
        return self.title


class NewspaperEdition(models.Model):
    published_date = models.DateField()
    articles = models.ManyToManyField(Article, related_name="editions")
    price = models.FloatField()

    def __str__(self):
        return f"Local newspaper edition published {self.published_date}"
