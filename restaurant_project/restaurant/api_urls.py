from django.urls import path
from . import api_views

urlpatterns = [
    path('menu/', api_views.MenuListCreate.as_view()),
    path('bookings/', api_views.BookingListCreate.as_view()),
]
