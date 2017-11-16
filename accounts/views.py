from .forms import ClientCreationForm
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = "accounts/home.html"
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

class RegisterView(CreateView):
    template_name = "accounts/reg_form.html"
    form_class = ClientCreationForm
    success_url = '/account/'
