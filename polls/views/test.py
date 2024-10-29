# Create your views here.
from ..models import Question
from django.views import generic


class TestView(generic.DetailView):
    model = Question
    template_name = "polls/test.html"
