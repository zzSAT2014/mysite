from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .models import Question, Choice
import os
# Create your views here.


def index(request):
    latest_question_list = Question.objects.all()[:5]
    template = loader.get_template('poll/index.html')
    context = RequestContext(request, {'latest_question_list': latest_question_list})

    return HttpResponse(template.render(context))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "poll/detail.html", {'question': question})


def results(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/result.html', {'question': q})


def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
        choice = q.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'poll/detial.html', {'question': q,
                                                    'error_message': 'your choice is invalid'})
    choice.votes += 1
    choice.save()
    # return render(request, 'poll/result.html', {'question': q})
    return results(request, question_id)


def get_jpg():
    base_dir = '/Users/Zhe/study/ol/'
    allfile = os.listdir(base_dir)
    return [os.path.join(base_dir, f) for f in filter(lambda f: f.endswith('.jpg'), allfile)]


def ol(request):
    allpics = get_jpg()
    return render(request, 'poll/ol.html', {'allpics': allpics})



