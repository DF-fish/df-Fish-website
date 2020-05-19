from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from articles.models import Article

### A Django view organizes the db objects

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'

class ArticleDetailView(DetailView):
    model = Article
