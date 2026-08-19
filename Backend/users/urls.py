from django.urls import path
from django.http import HttpResponse

def test(request):
    return HttpResponse("Users app working")

urlpatterns = [
    path("test/", test),
]