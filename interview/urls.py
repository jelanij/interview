from django.urls import include, path
from . import views

urlpatterns = [
path('interview',views.index),
path('',views.index),
path('get_data',views.get_data)
]