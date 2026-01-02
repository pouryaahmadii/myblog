from django.urls import path, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='blog'),
    re_path(r'^(?P<slug>[-\w\u0600-\u06FF]+)/$', views.ArticleDetailView.as_view(), name='article'),
]