#parkingapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('spots/<str:spot_type>/', views.spot_list, name='spot_list'),
    path('reserve/<int:spot_id>/', views.reserve_spot, name='reserve_spot'),
    # path('logout', views.logout,name='logout'),
]
