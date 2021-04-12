from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.
def add_show(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            reg = User(name=name, email=email, password=password)
            reg.save()
            form = StudentRegistration()
    else:
        form = StudentRegistration()
    stud = User.objects.all()
    context = {'form': form, 'stud': stud}
    return render(request, 'enroll/addandshow.html', context)


def update_data(request, id):
    if request.method == 'POST':
        items = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=items)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        items = User.objects.get(pk=id)
        form = StudentRegistration(instance=items)

    return render(request, 'enroll/updatestudent.html', {'form': form})


def delete_data(request, id):
    if request.method == "POST":
        form = User.objects.get(pk=id)
        form.delete()
        return redirect('/')
