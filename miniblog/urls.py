from django.urls import path
from .views import IndexView, register, logout_user, login_user, edit_profile, profile, delete_profile, create_post

app_name = 'miniblog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    path('edit-profile/', edit_profile, name='edit-profile'),
    path('delete-profile/', delete_profile, name='delete-profile'),
    path('profile/', profile, name='profile'),
    path('create/', create_post, name='create_post'),
]