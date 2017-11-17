from .forms import ClientCreationForm
from django.views.generic import CreateView

# Create your views here.
class RegisterView(CreateView):
    template_name = "accounts/reg_form.html"
    form_class = ClientCreationForm
    success_url = '/'
