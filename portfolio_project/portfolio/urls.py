from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('services/', views.ServiceListView.as_view(), name='services'),
    path('portfolio/', views.ProjectListView.as_view(), name='portfolio'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
