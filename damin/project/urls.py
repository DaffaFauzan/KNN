from django.urls import path
from . import views

app_name = 'project'
urlpatterns = [
	# ex: /project/
    path('', views.dashboard, name='dashboard'),
    path('proses', views.proses, name='proses'),
    path('desc', views.desc, name='desc'),
    path('table', views.table, name='table'),
    path('visualisasi', views.visualisasi, name='visualisasi'),
    path('data', views.data, name='data'),
]