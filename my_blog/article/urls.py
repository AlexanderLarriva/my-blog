from django.urls import path
from .views import index, HomePageView
# from my_blog.article import views

urlpatterns = [
    # path('', views.index),
    # path('index/', views.index, name='articles_index'),
    # path('', index.as_view()),
    # path('index/', index.as_view(), name='articles_index'),
    path('', HomePageView.as_view()),
    path('<str:tags>/<int:article_id>', index.as_view(), name='article'),
]