from django.urls import path
from .views import predict, history

urlpatterns = [
    path("predict/", predict, name="predict"),
    path("history/", history, name="history"),
]