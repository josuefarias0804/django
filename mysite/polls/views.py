from django.core.serializers import json
from django.template import loader
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, Http404, StreamingHttpResponse, JsonResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views import generic


from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    def post(request):
        if request.method == 'POST':
            # received_json_data = json.loads(request.POST['data'])
            # received_json_data=json.loads(request.body)
            return StreamingHttpResponse('it was post request: ')
        return StreamingHttpResponse('it was GET request')


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def detail(request, question_id):
    def detail(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def question1(request, question_id):
    try:
        question = get_object_or_404(Question, pk=question_id)
    except Http404:
        return JsonResponse({'error': 'No encontrado'}, status=404)
    return HttpResponse(question.to_json())
    # return render(request, 'polls/question1.html', {'question': question})
