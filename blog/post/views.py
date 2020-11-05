from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from .models import Article

class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['articles'] = Article.objects.all()

        return context


class DetailPage(DetailView):
    template_name = 'article.html'
    model = Article
    context_object_name = 'article'

