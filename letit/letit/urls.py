from django.contrib import admin
from django.urls import path, include
import zoom.views as views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('letitzoom/', views.site),
]