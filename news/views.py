from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from news.forms import (
    TopicNameSearchForm,
    RedactorUsernameSearchForm,
    RedactorForm,
    RedactorUpdateForm,
    ArticleForm,
    ArticleTitleSearchForm,
    NewspaperEditionForm,
    NewspaperEditionPriceSearchForm,
)
from news.models import (
    Redactor,
    Article,
    Topic,
    NewspaperEdition,
)


def index(request):
    num_redactors = Redactor.objects.count()
    num_articles = Article.objects.count()
    num_topics = Topic.objects.count()
    num_newspaper_editions = NewspaperEdition.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_redactors": num_redactors,
        "num_articles": num_articles,
        "num_topics": num_topics,
        "num_newspaper_editions": num_newspaper_editions,
        "num_visits": num_visits + 1,
    }

    return render(request, "news/index.html", context=context)


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "news/topic_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TopicNameSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        form = TopicNameSearchForm(self.request.GET)
        queryset = super().get_queryset()
        if form.is_valid():
            queryset = queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("news:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("news:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("news:topic-list")
    template_name = "news/topic_delete.html"


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RedactorListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = RedactorUsernameSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        form = RedactorUsernameSearchForm(self.request.GET)
        queryset = super().get_queryset()
        if form.is_valid():
            queryset = queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorForm


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorUpdateForm
    template_name = "news/redactor_form.html"
    success_url = reverse_lazy("news:redactor-detail")


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    template_name = "news/redactor_delete.html"
    success_url = reverse_lazy("news:redactor-list")


class ArticleListView(LoginRequiredMixin, generic.ListView):
    model = Article
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = ArticleTitleSearchForm(
            initial={"title": title}
        )
        return context

    def get_queryset(self):
        form = ArticleTitleSearchForm(self.request.GET)
        queryset = super().get_queryset()
        if form.is_valid():
            queryset = queryset.filter(
                title__icontains=form.cleaned_data["title"]
            )
        return queryset


class ArticleDetailView(LoginRequiredMixin, generic.DetailView):
    model = Article


class ArticleCreateView(LoginRequiredMixin, generic.CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy("news:article-list")


class ArticleUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy("news:article-list")


class ArticleDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Article
    template_name = "news/article_delete.html"
    success_url = reverse_lazy("news:article-list")


class NewspaperEditionListView(LoginRequiredMixin, generic.ListView):
    model = NewspaperEdition
    paginate_by = 3
    template_name = "news/newspaper_edition_list.html"
    context_object_name = "newspaper_edition_list"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(
            NewspaperEditionListView, self
        ).get_context_data(**kwargs)
        price = self.request.GET.get("price", "")
        context["search_form"] = NewspaperEditionPriceSearchForm(
            initial={"price": price}
        )
        return context

    def get_queryset(self):
        form = NewspaperEditionPriceSearchForm(self.request.GET)
        queryset = super().get_queryset()
        if form.is_valid():
            queryset = queryset.filter(
                price__contains=form.cleaned_data["price"]
            )
        return queryset


class NewspaperEditionDetailView(LoginRequiredMixin, generic.DetailView):
    model = NewspaperEdition
    template_name = "news/newspaper_edition_detail.html"
    context_object_name = "newspaper_edition"


class NewspaperEditionCreateView(LoginRequiredMixin, generic.CreateView):
    model = NewspaperEdition
    form_class = NewspaperEditionForm
    template_name = "news/newspaper_edition_form.html"
    success_url = reverse_lazy("news:newspaper-edition-list")


class NewspaperEditionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = NewspaperEdition
    form_class = NewspaperEditionForm
    success_url = reverse_lazy("news:newspaper-edition-list")
    template_name = "news/newspaper_edition_form.html"
    context_object_name = "newspaper_edition"


class NewspaperEditionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = NewspaperEdition
    template_name = "news/newspaper_edition_delete.html"
    success_url = reverse_lazy("news:newspaper-edition-list")
    context_object_name = "newspaper_edition"
