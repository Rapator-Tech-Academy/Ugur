from django.db import models 

class Category(models.Model):
    category = models.CharField(max_length=70, verbose_name="Category")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category