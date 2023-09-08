from django.urls import path
from myapp import views


urlpatterns = [
    
    path("register", views.register_request, name="register"),
]