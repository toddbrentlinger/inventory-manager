from django.shortcuts import render, get_object_or_404
from .models import User

def index(request):
    return render(request, 'index.html')

def user_detail_view(request, pk):
    user = get_object_or_404(User, pk=pk)

    context = {
        user,
    }

    return render(request, 'users/user_detail.html', context=context)
