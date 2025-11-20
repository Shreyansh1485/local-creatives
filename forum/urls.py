from django.urls import path
from . import views
urlpatterns = [
    path('', views.topic_list, name='topic_list'),
    path('create/', views.topic_create, name='topic_create'),
    path('<int:pk>/', views.topic_detail, name='topic_detail'),
    path('<int:pk>/reply/', views.reply_create, name='reply_create'),
]
