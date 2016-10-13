from django.conf.urls import include, url
from django.contrib import admin

import products.urls

urlpatterns = [
    url(r'^', include(products.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
