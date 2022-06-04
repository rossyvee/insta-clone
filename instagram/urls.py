from django.urls import path,include
from instagram import views


urlpatterns = [
    path('',views.index, name='home'),
]