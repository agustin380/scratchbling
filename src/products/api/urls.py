from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter
from rest_framework_jwt import views as auth_views

from . import views

router = DefaultRouter()
router.register(r'products', views.ProductsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/', auth_views.obtain_jwt_token)
]
