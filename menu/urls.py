from django.contrib import admin
from django.urls import path
from menu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.menu_view, name='menu'),
]