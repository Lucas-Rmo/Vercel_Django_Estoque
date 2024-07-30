from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from estoque import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login/logout.html'), name='logout'),
    path('register/', views.register, name='cadastro'),
    path('', include('estoque.urls')),
]
