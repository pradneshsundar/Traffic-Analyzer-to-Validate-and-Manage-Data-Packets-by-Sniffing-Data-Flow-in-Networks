from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('', views.landingpage, name='landingpage'),
    path('about/', views.about, name='about'),
    path('ishemic_cancer', views.ishemic_cancer, name='ishemic_cancer'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutusers, name='logout'),
    path('predict/', views.predict, name='Model'),
    


]
