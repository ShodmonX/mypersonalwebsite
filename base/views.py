from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse

from . import models
from . import forms

# Create your views here.
def HomePageView(request):
    articles = models.Article.objects.all()
    context = {'articles': articles}
    return render(request, 'pages/home.html', context)

def ArticlePageView(request, pk):
    article = models.Article.objects.get(url=pk)
    comments = models.Comment.objects.filter(article__url=pk)

    if request.method == 'POST':
        body = request.POST.get('body')
        if body:
            comment = models.Comment.objects.create(article=article, user=request.user, body=body)
            comment.save()



    context = {'article': article, 'comments': comments}
    return render(request, 'pages/article-details.html', context)

def ArticlePage(request):
    articles = models.Article.objects.all()
    context = {'articles': articles}
    return render(request, 'pages/article.html', context)

def LogoutPageView(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'pages/logout.html')

def LoginPageView(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = models.User.objects.get(username=username)
        except:
            pass
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            return redirect('home')

    context = {}
    return render(request, 'pages/login.html', context)


def SignupPageView(request):
    
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    form = forms.UserForm
    context = {'form': form}
    return render(request, 'pages/signup.html', context)


def CreateArticlePageView(request):
    if request.method == 'POST':
        form = forms.ArticleForm(request.POST, request.FILES) if request.FILES else forms.ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article-details', request.POST.get('url'))

    form = forms.ArticleForm
    context = {'form': form}
    return render(request, 'pages/create-article.html', context)

def DeleteArticlePageView(request, pk):
    article = models.Article.objects.get(url=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('home')

    context = {'response': article.title + " " + "article"}
    return render(request, 'pages/delete.html', context)


def DeleteCommentPageView(request, pk):
    comment = models.Comment.objects.get(id=pk)
    url = comment.article.url
    if request.method == 'POST':
        x = models.Comment.objects.get(id=pk)
        x.delete()
        return redirect('article-details', url)

    context = {'response': comment.body + " " + "comment"}
    return render(request, 'pages/delete.html', context)