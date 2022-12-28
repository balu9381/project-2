from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ravi(request):
    return HttpResponse('<h1>fan of raviteja</h1>')