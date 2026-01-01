from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/blog_list.html'
    context_object_name = "articles"
    queryset = Article.objects.all()
    ordering = ['-date']
    paginate_by = 1
    # paginate_orphans = 1


