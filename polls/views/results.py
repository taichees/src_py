# Create your views here.
from ..models import Question
from django.views import generic


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
