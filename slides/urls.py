from django.urls import path
from .views import presentation_view, feedback_view

urlpatterns = [
    path('<int:pk>', presentation_view),
    path('feedback', feedback_view),
]
