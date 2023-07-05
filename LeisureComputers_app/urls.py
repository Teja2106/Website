from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('apt-booking',views.Page2.as_view(), name='apt-booking'),
]
