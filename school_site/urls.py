from django.urls import path
from . import views


urlpatterns = [
    path('', views.ru_home, name='home_ru'),
    path('en/', views.en_home, name='home_en'),
    path('uz/', views.uz_home, name='home_uz'),
    path('circles/', views.ru_circles, name='circles_ru'),
    path('en/circles/', views.en_circles, name='circles_en'),
    path('uz/circles/', views.uz_circles, name='circles_uz'),
    path('teachers/', views.ru_teachers, name='teachers_ru'),
    path('en/teachers/', views.en_teachers, name='teachers_en'),
    path('uz/teachers/', views.uz_teachers, name='teachers_uz'),
    path('call-request/', views.ru_call_request, name='call-request_ru'),
    path('en/call-request/', views.en_call_request, name='call-request_en'),
    path('uz/call-request/', views.uz_call_request, name='call-request_uz'),
]
