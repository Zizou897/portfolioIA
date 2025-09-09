from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('blog/', views.ArticleListView.as_view(), name='blog_list'),
    path('blog/<slug:slug>/', views.ArticleDetailView.as_view(), name='blog_detail'),
]
