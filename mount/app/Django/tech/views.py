from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.views.generic.detail import DetailView
from .models import Article
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404


def index(request):
    template = loader.get_template('tech/article_list.html')
    context = {}
    return HttpResponse(template.render(context, request))


def post_detail(request, pk):
    post = get_object_or_404(Article, pk=pk)
    return render(request, 'tech/article_detail.html', {'post': post})


class ArticleDetailView(DetailView):
    model = Article


class ArticleList(ListView):
    model = Article
