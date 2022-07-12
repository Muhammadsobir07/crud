from django.urls import path
from .views import (
    register_page,
    create_profile,
    login_page,
    home,login,
    logout_user,
    delete,
)


urlpatterns = [
    path('sign_up',register_page, name="register_page"),
    path("create_profile",create_profile,name="create_profile"),
    path('login', login, name="login"),
    path('logout_user',logout_user,name="logout_user"),
    path('home/',home, name="home"),
    path('',login_page,name="login"),
    path('<int:id>/delete/',delete,name="delete"),
]