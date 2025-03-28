from django.urls import path
from .views import RegisterUserView, CustomAuthToken, ServiceRequestListCreateView

urlpatterns = [
    path('users/', RegisterUserView.as_view(), name='user-register'),
    path('auth/', CustomAuthToken.as_view(), name='auth-token'),
    path('service-requests/', ServiceRequestListCreateView.as_view(), name='service-request-list'),
]
