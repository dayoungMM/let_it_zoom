from django.contrib import admin
from django.urls import path, include
import zoom.views as views
urlpatterns = [
    
    path('letitzoom/', views.site),
    path('foodgame/', views.foodgame),


    path('admin/', admin.site.urls),
    path('data/', views.data, name='data'),
    path('score/', views.score, name='score'),

]

