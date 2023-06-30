from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from django.core.paginator import Paginator

def index(request):
    objects = Article.objects.all()
    paginator = Paginator(objects,2)
    page_number = request.GET.get('page')
    context = {
        'page_objects':paginator.get_page(page_number),
        'page_number':page_number,
    }

    return render(request, 'blog/blogs.html', context)


def article(request,pk):
    object = Article.objects.get(pk=pk)
    context = {
        'article':object
    }

    return render(request,'blog/article.html',context)
