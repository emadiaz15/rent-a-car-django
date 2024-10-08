from django.urls import path
from apps.cars.pages import views


urlpatterns = [
    path("", views.car_list_view, name="car_list_view"),
    path('<int:car_id>/', views.car_detail_view, name='car_detail_view'),
]