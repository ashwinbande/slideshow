from django.urls import path
from .views import presentation_view, feedback_view, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('<int:pk>', presentation_view, name='presentation'),
    path('feedback', feedback_view),
]
