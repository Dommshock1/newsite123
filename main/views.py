from django.shortcuts import render
from . import models



def index(request):
    categories = models.Category.objects.all()
    return render(request, 'main/index.html', {'categories': categories })  
