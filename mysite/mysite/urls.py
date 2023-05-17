from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('groad/', include('groad.urls')),
    path('admin/', admin.site.urls),
]
