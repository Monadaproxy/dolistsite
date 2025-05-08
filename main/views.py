from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    data = {
        'title': 'Главная страница',

    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

