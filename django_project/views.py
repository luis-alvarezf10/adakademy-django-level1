from django.views.generic import TemplateView

class HomeView(TemplateView):
    #obligatorio escribirlo asi
    template_name = 'home.html'