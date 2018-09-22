from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.models import User

# Create your views here.

def index(request):
    latest_user_list = User.objects.order_by('-date_joined')[:5]
    context = {'latest_user_list': latest_user_list}
    return render(request, 'users/index.html', context)

def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'users/detail.html', {'user': user})
