from django.urls import path
from . import views

urlpatterns = [
    path('corps/', views.CorpList.as_view()),
    path('esgscore/<ticker>/', views.EsgScoreDetail.as_view(), name='esg-score'),
]
