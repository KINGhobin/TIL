from django.shortcuts import render, redirect
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    return render(request, 'articles/create.html')

def new(request):
    # print(request.POST)
    # print(request.POST.get('title'))
    # print(request.POST.get('content'))

    # 1번 방법
    # article = Article()
    # article.title = request.GET.get('title')
    # article.content = request.GET.get('content')
    # article.save()
    # create에서 입력 후 index가보면 맨 밑에 입력값이 추가됨

    # 2번 방법
    # title = request.GET.get('title')
    # content = request.GET.get('content')
    # article = Article(title=title, content=content)
    # article.save()

    # 3번 방법
    title = request.POST.get('title')
    content = request.POST.get('content')

    Article.objects.create(title=title, content=content)

    # return render(request, 'articles/new.html')
    return redirect('articles:index')

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        "article" : article,
    }
    return render(request, 'articles/detail.html', context)

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        "article" : article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    edit_data = Article.objects.get(pk=pk)

    edit_data.title = request.POST.get('title')
    edit_data.content = request.POST.get('content')

    edit_data.save()

    return redirect('articles:detail', edit_data.pk)

def delete(request, pk):
    del_data = Article.objects.get(pk=pk)
    del_data.delete()

    return redirect('articles:index')