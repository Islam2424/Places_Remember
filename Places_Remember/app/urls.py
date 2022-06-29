from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
from Places_Remember.map.views import MapViews

app_name = 'map'

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', views.home, name='home'),
    path('home/map', MapViews.as_view(), name='map'),
    path('social-auth/', include('social_django.urls', namespace="social")),

]