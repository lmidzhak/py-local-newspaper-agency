from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from news.models import (
    Redactor,
    Article,
    Topic,
    NewspaperEdition,
)


@login_required
def index(request):
    """View function for the home page of the site."""

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
