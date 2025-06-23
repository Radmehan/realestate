from django.urls import path
from . import views

urlpatterns = [
    path("", views.properties, name="properties"),
    path("home single/<int:id>", views.home_single, name="home_single"),
    path("places/", views.places, name="places"),
    path("place single/<str:city>/", views.place_single, name="place_single"),
    path("place quick view/<int:id>", views.place_quick_view, name="place_quick_view"),
    
]