from django.urls import path

from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mahsulot/', views.mahsulot, name='mahsulot'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_page, name='login'),
    path('savat/', views.svat, name='savat'),
    path('detail/<int:pk>/', views.mahsulot_detail, name='form'),
    path('register', views.register_page, name='register'),
    path('confirm_password/', views.confirm_password, name='confirm_password'),
]