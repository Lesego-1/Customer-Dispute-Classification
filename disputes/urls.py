from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/predict/", views.predict_dispute, name="api_predict"),
]
