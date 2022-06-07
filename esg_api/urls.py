from django.urls import path
from . import views


urlpatterns = [
    path('corps/', views.corp_list),
    path('esgscore/<int:pk>/', views.esg_score, name='esg-score'),
]