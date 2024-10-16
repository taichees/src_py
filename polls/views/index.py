# Create your views here.
from ..models import Question
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(
            **kwargs
        )  # はじめに継承元のメソッドを呼び出す
        context["title"] = "indexTitle"
        return context
