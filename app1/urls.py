from django.urls import path

from . import views  # Import the views for this app

urlpatterns = [
	path('', views.index, name="index"),
]