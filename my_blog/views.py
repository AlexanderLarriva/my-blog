from django.views import View
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse

# def index(request):
#     return render(request, 'index.html', context={
#         'who': 'World',
#     })


class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context
    
class HomeRedirectView(View):
    def get(self, request, *args, **kwargs):
        # Используйте reverse для получения URL по имени маршрута 'article' с параметрами
        url = reverse('article', kwargs={'tags': 'python', 'article_id': 42})
        # Выполните перенаправление на полученный URL
        return redirect(url)


def about(request):
    return render(request, 'about.html')