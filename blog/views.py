from django.shortcuts import render
from django.views.generic import ListView, DetailView

from account.models import Profile
from blog.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/blog_list.html'
    context_object_name = "articles"
    queryset = Article.objects.all()
    ordering = ['-date']
    paginate_by = 1
    paginate_orphans = 1

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/blog_detail.html'
    context_object_name = 'article'
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.author:
            context['related_article'] = Article.objects.filter(author=self.object.author).exclude(pk=self.object.pk)
            context['author_profile'] = Profile.objects.get(user=self.object.author)
        else:
            context['related_article'] = []
            context['author_profile'] = None

        return context
