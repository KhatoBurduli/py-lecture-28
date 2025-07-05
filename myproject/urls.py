from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

from human.views import human_list


def home(request):
    return HttpResponse("My project")

urlpatterns = [
    path('',home),
    path('admin/', admin.site.urls),
    path('api/',include('poll.urls')),
    path('human_list/', human_list, name="human_list")
]
