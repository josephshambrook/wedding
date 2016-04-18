from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404, render, get_list_or_404, render_to_response
from django.http import HttpResponseRedirect, Http404, HttpResponseNotFound, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.template import loader
from django.views import generic
from django.views.generic import FormView, TemplateView
from django import forms

# from .models import Choice, Question
from weddingapp.forms import ExtraForm
from .models import Invite, Guest


def get_invite(code):
    # Expects code to find invite with
    # is there a better function to use than this one with a 404?
    invite = get_object_or_404(Invite, code=code)

    if invite.rsvp_completed:
        # go to error page as rsvp completed
        raise Http404
    else:
        return invite


def index_view(request, code):
    invite = None

    try:
        invite = get_invite(code)
    except:
        raise Http404("Invite does not exist")

    context = {
        'invite': invite,
        'nextUrl': reverse('weddingapp:attend', args=[invite.code]),
    }
    return render(request, 'weddingapp/index.html', context)


def attend_view(request, code):
    invite = get_invite(code)

    if request.method == 'POST':
        print('\n POST submission detected')

        try:
            # loop through each guest and assign its attendance
            # get all guests that were shown, then all guests sent in the POST
            # make a comparison to find who's going and who's not
            guests = invite.guest_set.all()
            guests_attending = request.POST.getlist('attend')

            for guest in guests:
                guest.attending = guest.guest_name in guests_attending
                guest.save()

            print('\n')
        except (KeyError, Invite.DoesNotExist):
            # Redisplay the form.
            return render(request, 'weddingapp/attend.html', {
                'invite': invite,
                'error_message': "This invite does not exist.",
            })
        else:
            print(guests_attending)
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            # go to Extras page
            return HttpResponseRedirect('extra')
    else:
        return render(request, 'weddingapp/attend.html', {
            'invite': invite,
        })


def extra_view(request, code):
    # Get the specific invite
    invite = get_invite(code)

    # Get guests attached to this invite
    guests = invite.guest_set.all()

    # Get the context from the request.
    context = RequestContext(request)

    # Store guests attending object
    guests_attending = invite.guest_set.filter(attending=True, invite=invite)

    if request.method == 'POST':
        form = ExtraForm(request.POST)

        print(form.data)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            print(form)

            return render(request, 'weddingapp/confirm.html', {
                'invite': invite,
            })
        else:
            # The supplied form contained errors - just print them to the terminal for now
            print form.errors

    # If the request was not a POST, display the form to enter details.
    guest_formset = modelformset_factory(Guest, form=ExtraForm)

    print "count: ", guest_formset.total_form_count(guest_formset())

    filtered_guest_form = guest_formset(queryset=guests.filter(attending=True))

    # print filtered_guest_form

    # print invite.code
    # print Guest.objects.filter(attending=True, invite = invite)

    return render_to_response('weddingapp/extra.html', {'GuestForm': filtered_guest_form, 'invite': invite,
                                                        'guests_attending': guests_attending}, context)

    # if request.method == 'POST':
    #     print('\n POST submission detected')
    #
    #     try:
    #
    #
    #         print('\n')
    #     except (KeyError, Invite.DoesNotExist):
    #         # Redisplay the form.
    #         return render(request, 'weddingapp/attend.html', {
    #             'invite': invite,
    #             'error_message': "This invite does not exist.",
    #         })
    #     else:
    #         print(guests_attending)
    #         # Always return an HttpResponseRedirect after successfully dealing
    #         # with POST data. This prevents data from being posted twice if a
    #         # user hits the Back button.
    #         return HttpResponseRedirect(reverse('weddingapp:vote.html'))
    # else:
    #     return render(request, 'weddingapp/extra.html', {
    #         'invite': invite,
    #     })


def confirm_view(request, code):
    invite = get_invite(code)
    return render(request, 'weddingapp/confirm.html', {
        'invite': invite,
    })


def finish_view(request, code):
    invite = get_invite(code)
    return render(request, 'weddingapp/finish.html', {
        'invite': invite,
    })

##
# class RsvpHome(models.Invite):
#     template_name = 'weddingapp/rsvp.html'
#     model = Invite


# class RsvpQuestion(generic.DetailView):
#     model = Question
#     template_name = 'weddingapp/question.html'


    # class DetailView(generic.DetailView):
    #     model = Question
    #     template_name = 'weddingapp/detail.html'


    # class ResultsView(generic.DetailView):
    #     model = Question
    #     template_name = 'weddingapp/results.html'


    # def vote(request, question_id):
    #     question = get_object_or_404(Question, pk=question_id)
    #     try:
    #         selected_choice = question.choice_set.get(pk=request.POST['choice'])
    #     except (KeyError, Choice.DoesNotExist):
    #         # Redisplay the question voting form.
    #         return render(request, 'weddingapp/detail.html', {
    #             'question': question,
    #             'error_message': "You didn't select a choice.",
    #         })
    #     else:
    #         selected_choice.votes += 1
    #         selected_choice.save()
    #         # Always return an HttpResponseRedirect after successfully dealing
    #         # with POST data. This prevents data from being posted twice if a
    #         # user hits the Back button.
    #         return HttpResponseRedirect(reverse('weddingapp:results.html', args=(question.id,)))
