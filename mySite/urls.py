from django.urls import path
from django.views.generic.base import RedirectView
from . import views

app_name = 'mySite'

urlpatterns = [
    path('favicon.ico/', RedirectView.as_view(url='/static/img/logoV2.png', permanent=True), name='favicon'),
    path('', views.index, name='index'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('post/<slug:slug>/', views.post, name='post'),
    path('<str:page_name>/', views.new_page, name='new_page'),
]