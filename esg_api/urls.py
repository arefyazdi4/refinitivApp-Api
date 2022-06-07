from django.urls import path
from . import views


urlpatterns = [
    path('corps/', views.corp_list),
    path('esgscore/<str:pk>/', views.esg_score),
]