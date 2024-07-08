from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('login/', views.login_view, name='login'),
    path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail'),
    path('photo/<int:photo_id>/like/', views.like_photo, name='like_photo'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('logout_confirm/', views.logout_confirm, name='logout_confirm'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
