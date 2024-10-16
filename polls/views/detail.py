# Create your views here.
from ..models import Question
from django.views import generic


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
