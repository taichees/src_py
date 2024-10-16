from django.urls import path

from .views import index
from .views import detail
from .views import results
from .views import vote

app_name = "polls"
urlpatterns = [
    path("", index.IndexView.as_view(), name="index"),
    path("<int:pk>/", detail.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", results.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", vote.vote, name="vote"),
]
