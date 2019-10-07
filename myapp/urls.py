from django.urls import path
from . import views

urlpatterns = [
    path('', views.summary, name='myapp-summary'),
    path('individual/', views.individual, name='myapp-individual')
]