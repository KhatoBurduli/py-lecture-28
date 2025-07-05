from django.urls import path

from poll import views

urlpatterns = [
    path('person',views.index)
]