from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about', views.about, name='about'),
    path('product', views.product, name='product'),
    path('contact', views.contact, name='contact'),
    path('why', views.why, name='why'),
    path('categary/<str:slug>', views.categary , name="categary"),
    path('reistration', views.reistration, name='reistration'),
    path('login', views.login, name='login'),
    path('search', views.search, name='search')
    
]
