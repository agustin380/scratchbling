from django.conf.urls import include, url
import products.api.urls


urlpatterns = [
    url(r'^api/', include(products.api.urls)),
]
