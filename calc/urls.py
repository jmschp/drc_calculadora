from django.urls import path
from . import views

app_name = "calc"

urlpatterns = [
    path('', views.index, name='index'),
    path('calc_dosagem', views.calc_dosagem, name='calc_dosagem'),
    path('calc_resultado', views.calc_dosagem, name='calc_resultado')
]
