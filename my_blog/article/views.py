from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.shortcuts import redirect
# from django.http import HttpResponse

# Create your views here.
# def index(request):
#     # return HttpResponse('article')
#     return render(request, '.html', context={name})

# def index(request):
#     name = 'my_blog.article'
#     return render(request, 'articles/index.html', context = {'app_name': name})


class index(View):
    
    # def get(self, request, *args, **kwargs):
    #     name = 'my_blog.article'
    #     return render(request, 'articles/index.html', context = {'app_name': name})
    
    def get(self, request, tags, article_id, *args, **kwargs):
        # Используем параметры tags и article_id в логике
        # просто формируем текст с использованием этих параметров
        result_text = f"Статья номер {article_id}. Тег {tags}"
        return render(request, 'articles/index.html', context={'result_text': result_text})
    
    



class HomePageView(View):
    # template_name = "index.html"

    def get(self, request, *args, **kwargs):
        # Получаем URL по имени маршрута 'article' с параметрами тега 'python' и ID статьи '42'
        url = reverse('article', kwargs={'tags': 'python', 'article_id': 42})
        # Выполняем перенаправление на полученный URL
        return redirect(url)

