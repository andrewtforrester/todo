from django.shortcuts import render
from .models import Person

# Create your views here.
def index(request):

    context = {
        'first_name': Person.objects.filter(first_name='Tom').first().first_name,
        'last_name': Person.objects.filter(first_name='Tom').first().last_name
    }

    return render(request, 'todoapp/index.html', context)