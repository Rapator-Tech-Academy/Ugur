from django.db import models
from django.utils import timezone

from .category import Category


class Article(models.Model):
    title = models.CharField(max_length=40, verbose_name="Title")
    body = models.TextField(verbose_name="Body of article")
    post_image = models.ImageField(null=True)
    pub_date = models.DateTimeField(auto_now=timezone.now())
    slug = models.SlugField(null=True, unique=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)


    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title