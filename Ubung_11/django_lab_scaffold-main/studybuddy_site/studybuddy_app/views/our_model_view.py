from django.views import generic
from .models import OurModel


class YourModelListView(generic.ListView):
    model = OurModel
    template_name = 'our_model_list.html'
    context_object_name = 'our_model_list'
