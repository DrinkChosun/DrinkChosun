from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Store

# Create your views here.
def index(request):
    stores = get_list_or_404(Store)
    context = {
        'stores': stores
    }
    return render(request, 'stores/index.html', context)
