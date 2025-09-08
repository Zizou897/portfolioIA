from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('portfolio/', views.ProjectListView.as_view(), name='portfolio'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('blog/', views.ArticleListView.as_view(), name='blog_list'),
    path('blog/<slug:slug>/', views.ArticleDetailView.as_view(), name='blog_detail'),
]
