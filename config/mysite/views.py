from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import Article
from django.contrib.auth.views import LoginView
from mysite.forms import UserCreationForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

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

    def form_valid(self, form):
        messages.success(self.request,'ログイン完了！！！')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,'エラーあり！！！')
        return super().form_invalid(form)

def singup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            user.save()
            #ログインさせる
            login(request,user)
            messages.success(request,'登録完了！！！')

            return redirect('/')

    return render(request, 'mysite/auth.html', context)

@login_required
def mypage(request):
    context = {}
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile  = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request,'更新完了しました')
    return render(request, 'mysite/mypage.html', context)