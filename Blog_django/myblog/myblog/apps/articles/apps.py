from django.apps import AppConfig


class ArticlesConfig(AppConfig):
    name = 'articles'

    # change language in admin panel - "ARTICLES"
    verbose_name = 'Blog'
