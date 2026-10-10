from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('videos/', views.videos, name='videos'),

    path('about/', views.about, name='about'),

    path('news/<int:id>/', views.news_detail, name='news_detail'),

    path('categories/', views.categories, name='categories'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
]