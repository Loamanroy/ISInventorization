from django.contrib import admin
from django.urls import path

from inventorization.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/cataloglist', CatalogAPIList.as_view()),
    path('api/v1/cataloglist/<int:pk>', CatalogAPIList.as_view())
]
