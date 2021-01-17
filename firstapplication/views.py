from django.shortcuts import render

# Create your views here.

def home(request):
    context = {'tag_var':'tag_var'}
    return render(request,"main.html",context)

