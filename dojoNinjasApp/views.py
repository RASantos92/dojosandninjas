from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    context = {
        "allTheDojos": Dojo.objects.all(),
        "allTheNinjas": Ninja.objects.all()
    }
    return render(request, "index.html", context)

def addDojo(request):
    Dojo.objects.create(name=request.POST['name'],location=request.POST['location'],guild=request.POST['guild'])
    return redirect('/')

def addNinja(request):
    Ninja.objects.create(name=request.POST['name'],age=request.POST['age'],dojo=Dojo.objects.get(id=request.POST['dojo']))
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')
