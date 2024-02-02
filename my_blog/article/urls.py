from django.urls import path
from my_blog.article import views
from .views import IndexView
# from my_blog.article import views

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:id>/', views.ArticleView.as_view(), name='article_view'),
    # path('index/', views.index, name='articles_index'),
    # path('', views.index.as_view()),
    # path('index/', index.as_view(), name='articles_index'),
    # path('', HomePageView.as_view()),
    path('<str:tags>/<int:article_id>/', views.index.as_view(), name='article'),
]