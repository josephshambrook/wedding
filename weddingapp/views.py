from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import FormView

from weddingapp import models
from .models import Choice, Question
from .models import Invite, Guest


class IndexView(generic.ListView):
    template_name = 'weddingapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


##
# class RsvpHome(models.Invite):
#     template_name = 'weddingapp/rsvp.html'
#     model = Invite


# class RsvpQuestion(generic.DetailView):
#     model = Question
#     template_name = 'weddingapp/question.html'


class DetailView(generic.DetailView):
    model = Question
    template_name = 'weddingapp/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'weddingapp/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'weddingapp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('weddingapp:results.html', args=(question.id,)))