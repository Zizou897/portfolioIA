from django.views.generic import TemplateView, ListView, View, DetailView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Service, Project, Article, HeroSection
from .forms import ContactForm

class HomePageView(View):
    template_name = "portfolio/home.html"
    form_class = ContactForm

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<div id="contact-form-wrapper" class="text-green-600 font-bold p-4 bg-green-100 rounded-md">Merci ! Votre message a été envoyé avec succès.</div>')

        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = {}
        context['hero_section'] = HeroSection.objects.first()
        context['latest_articles'] = Article.objects.order_by('-created_at')[:3]
        context['projects'] = Project.objects.order_by('-created_at')
        context['form'] = self.form_class()
        return context


class ArticleListView(ListView):
    model = Article
    template_name = 'portfolio/blog_list.html'
    context_object_name = 'articles'
    paginate_by = 5

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'portfolio/blog_detail.html'
    context_object_name = 'article'
