from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"
        ordering = ["username"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.username}"

    def get_absolute_url(self):
        return reverse("news:redactor-detail", kwargs={"pk": self.pk})


class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    topics = models.ManyToManyField(Topic, related_name="articles")
    redactors = models.ManyToManyField(Redactor, related_name="articles")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news:article-detail", kwargs={"pk": self.pk})


class NewspaperEdition(models.Model):
    edition = models.IntegerField(default=1)
    published_date = models.DateField(auto_now=True)
    articles = models.ManyToManyField(Article, related_name="editions")
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ["edition"]

    def __str__(self):
        return (
            f"Local newspaper edition number {self.edition},"
            f" published {self.published_date}"
        )

    def get_absolute_url(self):
        return reverse("news:newspaper-edition-detail", kwargs={"pk": self.pk})
