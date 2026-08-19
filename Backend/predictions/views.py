from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Prediction
from ml_model.predictor import predict_price


@api_view(["POST"])
def predict(request):
    area = request.data.get("area")
    bedrooms = request.data.get("bedrooms")
    bathrooms = request.data.get("bathrooms")
    location = request.data.get("location")

    price = predict_price(area, bedrooms, bathrooms, location)

    Prediction.objects.create(
        area=area,
        bedrooms=bedrooms,
        bathrooms=bathrooms,
        location=location,
        predicted_price=price
    )

    return Response({
        "predicted_price": price
    })


@api_view(["GET"])
def history(request):
    data = Prediction.objects.values().order_by("-created_at")
    return Response(list(data))