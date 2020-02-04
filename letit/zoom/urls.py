from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('letitzoom/', views.site),
]