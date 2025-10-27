from django.urls import path
from . import views

urlpatterns = [
    path('cameras/', views.CameraListAPIView.as_view(), name='camera-list'),
    path('cameras/create/', views.CameraCreateAPIView.as_view(), name='camera-create'),
    path('cameras/<int:pk>/', views.CameraRetrieveAPIView.as_view(), name='camera-detail'),
    path('cameras/<int:pk>/update/', views.CameraUpdateAPIView.as_view(), name='camera-update'),
    path('cameras/<int:pk>/delete/', views.CameraDestroyAPIView.as_view(), name='camera-delete'),
]