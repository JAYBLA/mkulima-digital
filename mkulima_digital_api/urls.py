from django.urls import path, include
from .views import (
    FeedbackApiView,
)


urlpatterns = [
    path('feedback/', FeedbackApiView.as_view()),
]


#'/api/v1/mkulima'