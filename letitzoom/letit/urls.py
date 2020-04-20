from django.contrib import admin
from django.urls import path, include
import zoom.views as views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('letitzoom/', views.site),
    path('data/', views.data, name='data'),
    path('answer/', views.answer, name='answer'),
    path('finalscore/', views.finalscore, name='finalscore'),
    path('score/', views.score, name='score'),
]

