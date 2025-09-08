from django.views.generic import TemplateView, ListView, View, DetailView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Service, Project, Article
from .forms import ContactForm

from .forms import ContactForm

class HomePageView(TemplateView):
    template_name = "portfolio/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.order_by('-created_at')[:3]
        context['projects'] = Project.objects.order_by('-created_at')
        context['form'] = ContactForm()
        return context

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/portfolio.html'
    context_object_name = 'projects'
    queryset = Project.objects.order_by('-created_at')

class ContactView(View):
    form_class = ContactForm
    template_name = 'portfolio/contact.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # Return a success message inside the original wrapper for HTMX
            return HttpResponse('<div id="contact-form-wrapper" class="text-green-600 font-bold p-4 bg-green-100 rounded-md">Merci ! Votre message a été envoyé avec succès.</div>')

        # If form is invalid, re-render the form part with errors
        return render(request, 'portfolio/partials/contact_form.html', {'form': form})

class ArticleListView(ListView):
    model = Article
    template_name = 'portfolio/blog_list.html'
    context_object_name = 'articles'
    paginate_by = 5

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'portfolio/blog_detail.html'
    context_object_name = 'article'
