from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from news.models import Redactor, Article, Topic, NewspaperEdition


class RedactorForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )
        template_name = "news/redactor_form.html"


class RedactorUsernameSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"}),
    )


class RedactorUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = "__all__"
        template_name = "news/redactor_form.html"


class TopicNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )


class ArticleForm(forms.ModelForm):
    redactors = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    topics = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Article
        fields = "__all__"


class ArticleTitleSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title"}),
    )


class NewspaperEditionForm(forms.ModelForm):
    articles = forms.ModelMultipleChoiceField(
        queryset=Article.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = NewspaperEdition
        fields = "__all__"
        template_name = "news/newspaper_edition_form.html"


class NewspaperEditionPriceSearchForm(forms.Form):
    price = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by price"}),
    )
