 
from django.contrib import admin
from django.urls import path,include
from .views import ArticleList
urlpatterns = [
   
    path('articles', ArticleList.as_view()),
  #  path('articles/<int:pk>', ArticleDetails.as_view() ),

   # path('articles/<int:pk>', article_detail),


]
