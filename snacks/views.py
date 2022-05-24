from django.views.generic import TemplateView

# give me some markup (template) and i will render in browser

class HomePageView(TemplateView):
  template_name = 'home.html'


class AboutPageView(TemplateView):
  template_name = 'about.html'