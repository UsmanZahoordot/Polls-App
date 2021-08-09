from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice


# Create your views here.

def index(request):
    qstObj = Question.objects.all()
    return render(request, 'polls/index.html', {'qst': qstObj})


def show_choices(request, question_id):
    qstObj = Question.objects.get(pk=question_id)
    return render(request, 'polls/choice.html', {'choice': qstObj})


def voted(request, question_id):
    if request.method == "POST":
        qstObj = Question.objects.get(pk=question_id)
        try:
            choiceObj = get_object_or_404(Choice, pk=request.POST['choice'])
        except:
            return HttpResponse("Please sleect an option")
        else:
            choiceObj.votes += 1
            choiceObj.save()
            return render(request, 'polls/choice.html', {'choice': qstObj})
    return render(request, 'polls/choice.html')
