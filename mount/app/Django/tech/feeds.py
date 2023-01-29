from django.contrib.syndication.views import Feed

from .models import Article

class LatestPostsFeed(Feed):
    title = "最新ブログ記事"
    link = ""
    description = "記事の最新情報をお届けします。"

    def items(self):
        return Article.objects.order_by('-publish_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content