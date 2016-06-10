from django.conf import settings
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.utils import translation
from django.utils.translation import check_for_language

from weddingapp.forms import ExtraForm
from .models import Invite, Guest


siteLanguages = (('en', 'English'), ('da', 'Danish'))


def set_language(request):
    next = request.META.get('HTTP_REFERER', None)
    response = HttpResponseRedirect(next)

    if request.method == 'GET':
        lang_code = request.GET.get('language', None)
        if lang_code and check_for_language(lang_code):
            if hasattr(request, 'session'):
                request.session['django_language'] = lang_code
            else:
                response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
            translation.activate(lang_code)
    return reverse()


def faq_index(request):
    # automatic redirect (could've done this in .htaccess but meh)
    return HttpResponseRedirect('practical')


def faq_practical(request):
    context = {
        'page': 'practical'
    }
    return render(request, 'weddingapp/practical.html', context)


def faq_cultural(request):
    return render(request, 'weddingapp/cultural.html', {'page': 'cultural'})


def get_invite(code):
    # Expects code to find invite with
    try:
        invite = Invite.objects.get(code=code)
    except Invite.DoesNotExist:
        return None

    return invite


def check_invite(invite):
    if invite is None:
        # if the invite doesn't exist, return a 404
        raise Http404("Invite does not exist")

    if invite.rsvp_completed:
        print 'rsvp is complete, trying to redirect'
        # if the invite has been completed, redirect to the finish page
        # return HttpResponseRedirect(reverse('weddingapp:finish', args=(invite.code,)))
        # finish_view(request, invite.code)
        return redirect('weddingapp:finish', code=invite.code)


def home_view(request):
    return render_to_response('weddingapp/home.html')


def index_view(request):
    if request.method == 'POST':
        code = request.POST['code']
        requested_invite = get_invite(code)

        if requested_invite is None:
            return render(request, 'weddingapp/index.html', {
                'does_not_exist': True,
                'code': code
            })
        else:
            return HttpResponseRedirect(reverse('weddingapp:welcome', args=(code,)))
    else:
        return render(request, 'weddingapp/index.html', {})


def welcome_view(request, code):
    invite = get_invite(code)
    check_invite(invite)

    context = {
        'invite': invite,
        # 'nextUrl': reverse('weddingapp:attend', args=[invite.code]),
    }
    return render(request, 'weddingapp/welcome.html', context)


def attend_view(request, code):
    invite = get_invite(code)

    if check_invite(invite):

        if request.method == 'POST':
            try:
                # loop through each guest and assign its attendance
                # get all guests that were shown, then all guests sent in the POST
                # make a comparison to find who's going and who's not
                guests = invite.guest_set.all()
                guests_attending = request.POST.getlist('attend')

                for guest in guests:
                    guest.attending = guest.guest_name in guests_attending
                    guest.save()
            except (KeyError, Invite.DoesNotExist):
                # Redisplay the form.
                return render(request, 'weddingapp/attend.html', {
                    'invite': invite,
                    'error_message': "This invite does not exist.",
                })
            else:
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
    check_invite(invite)

    # Get the context from the request.
    context = RequestContext(request)

    # Store guests attending object
    guests_attending = invite.guest_set.filter(attending=True, invite=invite)

    # Create the formset for each Guest
    GuestFormset = inlineformset_factory(Invite, Guest,
                                         form=ExtraForm,
                                         fields=('diet', 'transport'),
                                         extra=0,
                                         can_delete=False)

    if request.method == "POST":
        formset = GuestFormset(request.POST, request.FILES,
                               instance=invite,
                               queryset=Guest.objects.filter(attending=1))

        if formset.is_valid():
            # Save the data to the database.
            formset.save()

            # Go to Confirm page
            return HttpResponseRedirect('confirm')
        else:
            # The supplied form contained errors - just print them to the terminal for now
            print formset.errors

    if guests_attending.count() > 0:
        formset = GuestFormset(instance=invite, queryset=Guest.objects.filter(attending=1))

        # Return the view
        return render_to_response('weddingapp/extra.html', {
            'GuestForm': formset,
            'invite': invite,
            'guests_attending': guests_attending,
            'errors': formset.errors
        }, context)
    else:
        # Since there's no guests to create a form for, return Confirm view
        return render(request, 'weddingapp/confirm.html', {
            'invite': invite,
        })


def confirm_view(request, code):
    invite = get_invite(code)
    check_invite(invite)

    return render(request, 'weddingapp/confirm.html', {
        'invite': invite,
    })


def finish_view(request, code):
    invite = get_invite(code)

    print invite.rsvp_completed

    if invite is not None and invite.rsvp_completed is False:
        invite.rsvp_completed = True
        invite.save()

    return render(request, 'weddingapp/finish.html', {
        'invite': invite,
    })
