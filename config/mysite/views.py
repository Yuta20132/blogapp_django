from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from django.contrib.auth.views import LoginView
from mysite.forms import UserCreationForm


# Create your views here.
def index(request):
    objects = Article.objects.all()[:3]
    context ={
        'title':'Really Site',
        'articles': objects
    }

    return render(request, 'mysite/index.html',context)

class Login(LoginView):
    template_name = 'mysite/auth.html'

def singup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            user.save()

    return render(request, 'mysite/auth.html', context)