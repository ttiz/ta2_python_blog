from django.db import models
from django.utils import timezone
from django.urls import reverse
import markdown


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_public = models.BooleanField(default=True)
    publish_date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ["-publish_date"]

    def __str__(self):
        return self.title

    def markdown_to_html(self):
        """Markdown を HTML に変換して出力
        さらに拡張機能を使用して目次を自動生成する"""

        md = markdown.Markdown(
            extensions=['extra', 'admonition', 'sane_lists', 'toc'])

        html: str = md.convert(self.content)
        return html

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk':self.pk})
