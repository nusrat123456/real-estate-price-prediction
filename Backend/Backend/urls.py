from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Real Estate Price Prediction API is Live!")

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("predictions/", include("predictions.urls")),
    path("users/", include("users.urls")),
]
