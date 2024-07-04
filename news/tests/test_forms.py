from django.test import TestCase

from news.forms import (
    TopicNameSearchForm,
    ArticleTitleSearchForm,
    RedactorUsernameSearchForm,
    NewspaperEditionPriceSearchForm,
    RedactorForm,
)


class FormsTests(TestCase):
    def setUp(self):
        self.form_data = {
            "username": "new_user",
            "password1": "user1test",
            "password2": "user1test",
            "first_name": "Test_name",
            "last_name": "Test_last_name",
            "years_of_experience": 2,
        }

    def get_form(self, **kwargs):
        form_data = self.form_data.copy()
        form_data.update(kwargs)
        return RedactorForm(data=form_data)

    def test_redactor_creation_form(self):
        form = RedactorForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, self.form_data)


class SearchFormsTests(TestCase):

    def test_redactor_search_form_valid(self):
        form_data = {"username": "test.user"}
        form = RedactorUsernameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "test.user")

    def test_redactor_search_form_empty(self):
        form_data = {"username": ""}
        form = RedactorUsernameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "")

    def test_article_search_form_valid(self):
        form_data = {"title": "test.title"}
        form = ArticleTitleSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["title"], "test.title")

    def test_article_search_form_empty(self):
        form_data = {"title": ""}
        form = ArticleTitleSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["title"], "")

    def test_topic_search_form_valid(self):
        form_data = {"name": "test.name"}
        form = TopicNameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "test.name")

    def test_topic_search_form_empty(self):
        form_data = {"name": ""}
        form = TopicNameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "")

    def test_newspaper_edition_search_form_valid(self):
        form_data = {"price": "1.00"}
        form = NewspaperEditionPriceSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["price"], "1.00")

    def test_newspaper_edition_search_form_empty(self):
        form_data = {"price": ""}
        form = NewspaperEditionPriceSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["price"], "")
