from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'message': 'Blog app works!'}
    return render(request, 'blog/index.html', context)
