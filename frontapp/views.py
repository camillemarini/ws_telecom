from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from frontapp.models import Probicipant
from frontapp.forms import ProbicipantForm

deadline_registration = 'March 18'
info_registration = 'March 22'


def index(request):
    return render(request, 'frontapp/index.html',
                  {'deadline_registration': deadline_registration})


def setup(request):
    return render(request, 'frontapp/requirements.html',
                  {'ola': 'ola'})


def registration(request):
    if request.method == 'POST':
        form = ProbicipantForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            subject = (u'Workshop Telecom - Scientific Programming with '
                       u'Python and Software Engineering Best Practices')
            message = (u'Thanks for your registration for the workshop '
                       u'in Telecom Paris about Scientific Programming with '
                       u'Python and Software Engineering Best Practices '
                       u'(28-29 April 2016)\n\n'
                       u'Due to limited space, we can accept 40 participants. '
                       u'Notification of acceptance will be sent by %s. ') \
                % (info_registration)
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER,
                          [email], fail_silently=False)
            except:
                pass
            return redirect("/registration_ok")
    else:
        form = ProbicipantForm()

    return render(request, 'frontapp/registration.html', {'form': form})


def registration_ok(request):
    return render(request, 'frontapp/registration_ok.html',
                  {'info_registration': info_registration})


@login_required
def registration_admin(request):
    list_probicipants = Probicipant.objects.all()
    list_prob = [[p, p.votes.exists(request.user)] for p in list_probicipants]
    context = {'list_probicipants': list_prob}
    return render(request, 'frontapp/registration_admin.html',
                  context)


def vote_up_down_probicipant(request, *args, **kwargs):
    prob_id = kwargs['probicipant_id']
    prob = Probicipant.objects.get(pk=prob_id)
    # make sure the user has already voted
    if prob.votes.exists(request.user):
        prob.votes.down(request.user)
    else:  # if he has not already voted
        prob.votes.up(request.user)
    return redirect('/registration_admin')
