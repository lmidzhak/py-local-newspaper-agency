from django.contrib.auth import get_user_model
from django.test import TestCase

from news.models import Topic, Redactor, Article, NewspaperEdition


class ModelsTests(TestCase):
    def test_topic_str(self):
        topic = Topic.objects.create(
            name="test_topic",
        )
        self.assertEqual(str(topic), f"{topic.name}")

    def test_redactor_str(self):
        redactor = Redactor.objects.create(
            username="test",
            password="test1234",
            first_name="test_first",
            last_name="test_last",
        )
        self.assertEqual(
            str(redactor),
            f"{redactor.first_name} "
            f"{redactor.last_name}: {redactor.username}",
        )

    def test_article_str(self):
        article = Article.objects.create(
            title="test_title",
            content="test_content",
        )
        self.assertEqual(str(article), article.title)

    def test_newspaper_edition_str(self):
        newspaper_edition = NewspaperEdition.objects.create(
            edition=1,
            published_date="2024-03-01",
            price=10.5,
        )
        self.assertEqual(
            str(newspaper_edition),
            f"Local newspaper edition number {newspaper_edition.edition},"
            f" published {newspaper_edition.published_date}",
        )

    def test_get_absolute_article_url(self):
        article = Article.objects.create(
            title="test_title",
            content="test_content",
        )
        self.assertEqual(
            article.get_absolute_url(),
            f"/articles/{article.id}/"
        )

    def test_get_absolute_redactor_url(self):
        redactor = get_user_model().objects.create_user(
            first_name="test_first_name",
            last_name="test_Last_name",
            years_of_experience=2,
            username="test_username",
        )
        self.assertEqual(
            redactor.get_absolute_url(),
            f"/redactors/{redactor.id}/"
        )

    def test_get_absolute_newspaper_edition_url(self):
        newspaper_edition = NewspaperEdition.objects.create(
            edition=1,
            published_date="2024-03-01",
            price=10.5,
        )
        self.assertEqual(
            newspaper_edition.get_absolute_url(),
            f"/newspaper-editions/{newspaper_edition.id}/",
        )
