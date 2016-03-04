from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from frontapp.forms import ProbicipantForm

deadline_registration = 'March 18'
info_registration = 'March 22'


def index(request):
    return render(request, 'frontapp/index.html',
                  {'deadline_registration': deadline_registration})


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
            send_mail(subject, message, settings.EMAIL_HOST_USER,
                      [email], fail_silently=False)
            return redirect("/registration_ok")
    else:
        form = ProbicipantForm()

    return render(request, 'frontapp/registration.html', {'form': form})


def registration_ok(request):
    return render(request, 'frontapp/registration_ok.html',
                  {'info_registration': info_registration})
