from django.urls import path
from .views import (
    register_page,
    create_profile,
    login_page,
    home,login,
    logout_user,
    user_delete,
    user_edit,
    user_edit_save,
)


urlpatterns = [
    path('sign_up',register_page, name="register_page"),
    path("create_profile",create_profile,name="create_profile"),
    path('login', login, name="login"),
    path('logout_user',logout_user,name="logout_user"),
    path('home/',home, name="home"),
    path('home/<int:id>',user_delete, name="user_delete"),
    path('home/edit/<int:id>',user_edit, name="user_edit"),
    path('user_edit_save',user_edit_save, name="user_edit_save"),
    path('',login_page,name="login"),
]