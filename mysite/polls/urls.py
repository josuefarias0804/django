from django.urls import path

from polls.views import ChoiceView
from . import views

urlpatterns = [
    # ex: /polls/
    path('home', views.index, name='index'),

    path('<int:question_id>/question1', views.question1, name='question1'),

    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]

app_name = 'polls'
urlpatterns = [
    path('index', views.IndexView.as_view(), name='index'),
    path('<int:question_id>/question1/', views.question1, name='question1'),
    path('choice', views.DetailView.as_view(), name='ChoiceView'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]