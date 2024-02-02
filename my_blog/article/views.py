from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse

from my_blog.article.models import Article

class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })



# from django.http import HttpResponse

# Create your views here.
# def index(request):
#     # return HttpResponse('article')
#     return render(request, '.html', context={name})

# def HomeArticle(request):
#     name = 'my_blog.article'
#     return render(request, 'articles/index.html', context = {'result_text': name})


class index(View):
    
    # def get(self, request, *args, **kwargs):
    #     name = 'my_blog.article'
    #     return render(request, 'articles/index.html', context = {'app_name': name})
    
    def get(self, request, tags, article_id, *args, **kwargs):
        # Используем параметры tags и article_id в логике
        # просто формируем текст с использованием этих параметров
        result_text = f"Статья номер {article_id}. Тег {tags}"
        return render(request, 'articles/index.html', context={'result_text': result_text})
    

class IndexView(View):
    
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })
    
    



class HomePageView(View):
    # template_name = "index.html"

    def get(self, request, *args, **kwargs):
        # Получаем URL по имени маршрута 'article' с параметрами тега 'python' и ID статьи '42'
        url = reverse('article', kwargs={'tags': 'python', 'article_id': 42})
        # Выполняем перенаправление на полученный URL
        return redirect(url)

