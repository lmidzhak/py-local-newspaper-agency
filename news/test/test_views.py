from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from news.models import Article, NewspaperEdition, Topic

TOPIC_URL = reverse("news:topic-list")
ARTICLE_URL = reverse("news:article-list")
REDACTOR_URL = reverse("news:redactor-list")
NEWSPAPER_EDITION_URL = reverse("news:newspaper-edition-list")


class PublicTopicTests(TestCase):

    def test_login_required(self):
        res = self.client.get(TOPIC_URL)
        self.assertNotEqual(res.status_code, 200)


class PublicArticleTests(TestCase):

    def test_login_required(self):
        res = self.client.get(ARTICLE_URL)
        self.assertNotEqual(res.status_code, 200)


class PublicRedactorTests(TestCase):

    def test_login_required(self):
        res = self.client.get(REDACTOR_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTopicTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="testuser", password="test1234"
        )
        self.client.force_login(self.user)

    def test_retrieve_topic(self):
        Topic.objects.create(name="weather")
        Topic.objects.create(name="business")
        response = self.client.get(TOPIC_URL)
        self.assertEqual(response.status_code, 200)
        topics = Topic.objects.all()
        self.assertEqual(
            list(response.context["topic_list"]),
            list(topics),
        )
        self.assertTemplateUsed(response, "news/topic_list.html")


class PrivateArticleTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="testuser", password="test1234"
        )
        self.client.force_login(self.user)

    def test_retrieve_article(self):
        Article.objects.create(title="where is rainbow?", content="weather")
        Article.objects.create(title="Bitcoin prospectives",
                               content="business")
        response = self.client.get(ARTICLE_URL)
        self.assertEqual(response.status_code, 200)
        articles = Article.objects.all()
        self.assertEqual(
            list(response.context["article_list"]),
            list(articles),
        )
        self.assertTemplateUsed(response, "news/article_list.html")


class PrivateRedactorTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="testuser", password="test1234"
        )
        self.client.force_login(self.user)

    def test_retrieve_redactor(self):
        get_user_model().objects.create_user(
            username="testuser1",
            password="test1233",
        )
        get_user_model().objects.create_user(
            username="testuser2",
            password="test1244",
        )
        response = self.client.get(REDACTOR_URL)
        self.assertEqual(response.status_code, 200)
        redactors = get_user_model().objects.all()
        self.assertEqual(
            list(response.context["redactor_list"]),
            list(redactors),
        )
        self.assertTemplateUsed(response, "news/redactor_list.html")

    def test_create_redactor(self):
        form_data = {
            "username": "new_user",
            "password1": "user1test",
            "password2": "user1test",
            "first_name": "Test_name",
            "last_name": "Test_last_name",
            "email": "abc@yes.com",
            "years_of_experience": 10,
        }
        self.client.post(reverse("news:redactor-create"), data=form_data)
        new_redactor = get_user_model().objects.get(
            username=form_data["username"]
        )

        self.assertEqual(new_redactor.first_name, form_data["first_name"])
        self.assertEqual(new_redactor.last_name, form_data["last_name"])
        self.assertEqual(
            new_redactor.years_of_experience, form_data["years_of_experience"]
        )


class PrivateNewspaperEditionTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="testuser", password="test1234"
        )
        self.client.force_login(self.user)

    def test_retrieve_newspaper_edition(self):
        NewspaperEdition.objects.create(
            edition=1, published_date="2024-06-30", price=10.50
        )
        NewspaperEdition.objects.create(
            edition=3, published_date="2024-07-01", price=11.30
        )
        response = self.client.get(NEWSPAPER_EDITION_URL)
        self.assertEqual(response.status_code, 200)
        newspaper_editions = NewspaperEdition.objects.all()
        self.assertEqual(
            list(response.context["newspaper_edition_list"]),
            list(newspaper_editions),
        )
        self.assertTemplateUsed(response, "news/newspaper_edition_list.html")
