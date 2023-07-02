

from django.contrib import admin
from django.urls import path,include
from mysite import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.index),
    path('blog/',include('blog.urls')),
    path('admin/',admin.site.urls),
    path('login/',views.Login.as_view()),
    path('logout/',LogoutView.as_view()),
    path('signup/',views.singup),
    path('mypage/',views.mypage),
]
