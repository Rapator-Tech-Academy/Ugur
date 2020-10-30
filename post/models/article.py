from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    body = models.CharField(max_length=240, verbose_name="Body of article")
    post_image = models.ImageField()

    class Meta:
        verbose_name = "Blog article"
        verbose_name_plural = "Blog articles"
    
    def __str__(self):
        return self.title
