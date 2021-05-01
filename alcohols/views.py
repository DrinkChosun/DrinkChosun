from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Alcohol

# Create your views here.
def index(request):
    alcohols = get_list_or_404(Alcohol)
    context = {
        'alcohols': alcohols,
    }
    return render(request, 'alcohols/index.html', context)