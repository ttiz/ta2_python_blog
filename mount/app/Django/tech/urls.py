from django.contrib import admin
from django.urls import path
from .feeds import LatestPostsFeed
from .views import ArticleDetailView
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from tech.models import Article

from . import views

info_dict= {
    'queryset': Article.objects.all(),
    'date_field': 'publish_date',
}

app_name = 'tech'
urlpatterns = [
    path('', views.ArticleList.as_view(), name='article'),
    path('admin/', admin.site.urls),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('sitemap.xml', sitemap, {'sitemaps': {'tech': GenericSitemap(info_dict)}},
         name='django.contrib.sitemaps.views.sitemap'),
    path('latest/feed/', LatestPostsFeed()),
]