from django.urls import path 
from Views import views

urlpatterns = [
    path("", views.index, name = 'index'),
    path("register", views.registration, name = 'register'),
    path("register_user", views.user_registration, name = 'user registration'),
    path("login", views.login, name = 'login'),
    path("login_user", views.login_user, name = 'user login'),
    path("search_title", views.search_title, name = 'title search'),
    path("view", views.view_book, name = "view book"),
    path("download", views.download, name = 'download')
]