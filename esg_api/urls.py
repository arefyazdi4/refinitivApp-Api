from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('corps', views.CorpViewSet)
router.register('esgscore', views.EsgScoreViewSet)
router.register('customers', views.CustomerViewSet)


urlpatterns = router.urls
