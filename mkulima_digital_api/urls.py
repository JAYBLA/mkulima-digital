from django.urls import path, include
from .views import (
    FeedbackApiView,
    TargetApiView,
    PembejeoApiView,
)


urlpatterns = [
    path('target/', TargetApiView.as_view()),
    path('pembejeo/', PembejeoApiView.as_view()),
    path('feedback/', FeedbackApiView.as_view()),
]


#'/api/v1/mkulima'