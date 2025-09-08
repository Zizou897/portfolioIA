from django.views.generic import TemplateView, ListView, View
from django.shortcuts import render
from django.http import HttpResponse
from .models import Service, Project
from .forms import ContactForm

class HomePageView(TemplateView):
    template_name = "portfolio/home.html"

class ServiceListView(ListView):
    model = Service
    template_name = 'portfolio/services.html'
    context_object_name = 'services'

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
