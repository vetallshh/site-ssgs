from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('indexTwo/', views.indexTwo, name='indexTwo'),
    path('legislation/', views.legislation, name='legislation'),
    path('documentsSro/', views.documentsSro, name='documentsSro'),
    path('compensationFund/', views.compensationFund, name='compensationFund'),
    path('registrySro/', views.registrySro, name='registrySro'), 
    path('ManagementBodies/', views.ManagementBodies, name='ManagementBodies'),
    path('intoSro/', views.intoSro, name='intoSro'), 
    path('termsStrah/', views.termsStrah, name='termsStrah'),
    path('vajnInfo/', views.vajnInfo, name='vajnInfo'),
    path('protocols/', views.protocols, name='protocols'),     
]


