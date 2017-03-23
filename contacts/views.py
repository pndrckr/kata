from django.shortcuts import render, get_list_or_404, redirect
from .models import Person

# Create your views here.
def index(request):
    return render(request, "index.html")