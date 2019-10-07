from django.shortcuts import render
from .models import microbit, microbitsummary
# Create your views here

tables = [
    {
    },
]

def summary(request):
    context = {
        'tables': microbitsummary.objects.all()
    }
    return render(request, 'myapp/summary.html', context)

def individual(request):
    context = {
        'tables': microbit.objects.all()
    }
    return render(request, 'myapp/individual.html', context)

def __str__(self):
    return self.title