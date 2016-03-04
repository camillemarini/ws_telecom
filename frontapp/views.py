from django.shortcuts import render, redirect
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
            return redirect("/registration_ok")
    else:
        form = ProbicipantForm()

    return render(request, 'frontapp/registration.html', {'form': form})


def registration_ok(request):
    return render(request, 'frontapp/registration_ok.html',
                  {'info_registration': info_registration})
