import datetime
from django.db import models
from django.utils import timezone

class Article(models.Model):
    article_title = models.CharField('name of article', max_length = 200)
    article_text = models.TextField('text of article')
    pub_date = models.DateTimeField('date of publication')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

    # change language in admin panel - "Articles"
    class Meta:
        verbose_name = 'Artykuł'
        verbose_name_plural = 'Artykuły'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('name of author', max_length = 50)
    comment_text = models.CharField('name of comment', max_length = 200)

    def __str__(self):
        return self.author_name

    # change language in admin panel - "Comments"
    class Meta:
        verbose_name = 'Komentarz'
        verbose_name_plural = 'Komentarze'
