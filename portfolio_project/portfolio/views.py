from django.views.generic import TemplateView, ListView
from .models import Service, Project

class HomePageView(TemplateView):
    template_name = "portfolio/home.html"

class AboutPageView(TemplateView):
    template_name = "portfolio/about.html"

class ServiceListView(ListView):
    model = Service
    template_name = 'portfolio/services.html'
    context_object_name = 'services'

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/portfolio.html'
    context_object_name = 'projects'
    queryset = Project.objects.order_by('-created_at')

class ContactView(TemplateView):
    template_name = "portfolio/contact.html"
